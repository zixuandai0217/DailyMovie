const api = require('../../utils/api.js');

Page({
  data: {
    movies: [],
    imageBaseUrl: 'https://image.tmdb.org/t/p/w200',
    searched: false
  },
  onSearch(e) {
    const query = e.detail.value;
    if (!query) return;
    
    wx.showLoading({ title: 'Searching...' });
    api.searchMovies(query).then(res => {
      this.setData({
        movies: res.movies || [],
        searched: true
      });
      wx.hideLoading();
    }).catch(err => {
      console.error(err);
      wx.hideLoading();
      wx.showToast({
        title: 'Search failed',
        icon: 'none'
      });
    });
  },
  goToDetail(e) {
    const id = e.currentTarget.dataset.id;
    wx.navigateTo({
      url: `/pages/detail/detail?id=${id}`
    });
  }
});
