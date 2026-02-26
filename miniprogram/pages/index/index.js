const api = require("../../utils/api.js");
const app = getApp();

Page({
  data: {
    movie: null,
    loading: false,
    error: null,
    posterError: false,
    backdropUrl: "",
    imageBaseUrl: "https://image.tmdb.org/t/p/w500",
    imageBackdropUrl: "https://image.tmdb.org/t/p/w1280",
    statusBarHeight: 0,
    navBarHeight: 44,
    totalNavHeight: 64, // Default fallback
  },
  onLoad() {
    this.setData({
      statusBarHeight: app.globalData.statusBarHeight,
      navBarHeight: app.globalData.navBarHeight,
      totalNavHeight: app.globalData.totalNavHeight,
    });
    this.fetchRandomMovie();
  },
  onPullDownRefresh() {
    this.fetchRandomMovie().then(() => {
      wx.stopPullDownRefresh();
    });
  },
  fetchRandomMovie() {
    this.setData({ loading: true, error: null });
    wx.showLoading({ title: "加载中...", mask: true });
    return api
      .getRandomMovie()
      .then((res) => {
        const movie = res.movie;
        let backdropUrl = "";
        if (movie) {
          const path = movie.backdrop_path || movie.poster_path;
          if (path) {
            backdropUrl = this.data.imageBackdropUrl + path;
          }
        }
        this.setData({
          movie: movie,
          backdropUrl: backdropUrl,
          posterError: false,
          loading: false,
        });
        wx.hideLoading();
      })
      .catch((err) => {
        console.error("Failed to fetch movie:", err);
        wx.hideLoading();
        this.setData({
          loading: false,
          error: "加载失败，请检查网络连接或后端服务是否运行",
        });
        wx.showToast({
          title: "加载失败",
          icon: "none",
        });
      });
  },
  refreshMovie() {
    this.fetchRandomMovie();
  },
  handlePosterError() {
    // Handle poster image load error gracefully
    this.setData({ posterError: true });
    console.warn("Poster image failed to load");
  },
});
