const api = require("../../utils/api.js");
const app = getApp();

Page({
  data: {
    user: null,
    genres: [
      { id: 28, name: "动作", icon: "⚔️" },
      { id: 35, name: "喜剧", icon: "😂" },
      { id: 18, name: "剧情", icon: "🎭" },
      { id: 878, name: "科幻", icon: "👽" },
      { id: 27, name: "恐怖", icon: "👻" },
      { id: 10749, name: "爱情", icon: "💘" },
    ],
    eras: [
      { value: "1980s", name: "80年代", icon: "📼" },
      { value: "1990s", name: "90年代", icon: "💾" },
      { value: "2000s", name: "2000年代", icon: "💿" },
      { value: "2010s", name: "2010年代+", icon: "📱" },
    ],
    keywords: "",
    selectedGenres: [],
    selectedEras: [],
    statusBarHeight: 0,
    navBarHeight: 44,
    totalNavHeight: 64,
    inputFocus: false,
  },

  onLoad() {
    this.setData({
      statusBarHeight: app.globalData.statusBarHeight,
      navBarHeight: app.globalData.navBarHeight,
      totalNavHeight: app.globalData.totalNavHeight,
    });
    const token = wx.getStorageSync("token");
    if (token) {
      this.fetchProfile(token);
    }
  },

  login() {
    wx.login({
      success: (res) => {
        if (res.code) {
          wx.showLoading({ title: "登录中..." });
          api
            .login(res.code, {})
            .then((data) => {
              wx.setStorageSync("token", data.token);
              this.setUserData(data.user);
              wx.hideLoading();
            })
            .catch((err) => {
              console.error(err);
              wx.hideLoading();
              wx.showToast({ title: "登录失败", icon: "none" });
            });
        }
      },
    });
  },

  fetchProfile(token) {
    api
      .getProfile(token)
      .then((user) => {
        this.setUserData(user);
      })
      .catch((err) => {
        console.error(err);
        // Token might be invalid
        wx.removeStorageSync("token");
        this.setData({ user: null });
      });
  },

  setUserData(user) {
    // Map preferences to UI state
    const prefs = user.preferences || {};
    const userGenres = prefs.genres || [];
    const userEras = prefs.decades || [];

    const genres = this.data.genres.map((g) => ({
      ...g,
      checked: userGenres.includes(g.id), // Note: ID types need to match
    }));

    const eras = this.data.eras.map((e) => ({
      ...e,
      checked: userEras.includes(e.value),
    }));

    this.setData({
      user,
      genres,
      eras,
      selectedGenres: userGenres,
      selectedEras: userEras,
      keywords: prefs.keywords || "",
    });
  },

  onGenreChange(e) {
    const selectedGenres = e.detail.value.map(Number);
    const genres = this.data.genres.map((g) => ({
      ...g,
      checked: selectedGenres.includes(g.id),
    }));
    this.setData({
      selectedGenres,
      genres,
    });
  },

  onEraChange(e) {
    const selectedEras = e.detail.value;
    const eras = this.data.eras.map((e) => ({
      ...e,
      checked: selectedEras.includes(e.value),
    }));
    this.setData({
      selectedEras,
      eras,
    });
  },

  focusInput() {
    this.setData({ inputFocus: true });
  },

  savePreferences() {
    const token = wx.getStorageSync("token");
    if (!token) return;

    const prefs = {
      genres: this.data.selectedGenres,
      decades: this.data.selectedEras,
      keywords: this.data.keywords,
    };

    wx.showLoading({ title: "保存中..." });
    api
      .updatePreferences(token, prefs)
      .then(() => {
        wx.hideLoading();
        wx.showToast({ title: "已保存!", icon: "success" });
      })
      .catch((err) => {
        wx.hideLoading();
        wx.showToast({ title: "保存失败", icon: "none" });
      });
  },

  logout() {
    wx.removeStorageSync("token");
    this.setData({ user: null });
  },
});
