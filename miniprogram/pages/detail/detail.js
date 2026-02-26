const api = require('../../utils/api.js');

Page({
  data: {
    movie: null,
    imageBaseUrl: 'https://image.tmdb.org/t/p/w500'
  },
  onLoad(options) {
    const id = options.id;
    if (id) {
      this.fetchMovieDetail(id);
    }
  },
  fetchMovieDetail(id) {
    wx.showLoading({ title: 'Loading...' });
    api.getMovieDetail(id).then(res => {
      this.setData({
        movie: res
      });
      wx.setNavigationBarTitle({
        title: res.title
      });
      wx.hideLoading();
    }).catch(err => {
      console.error(err);
      wx.hideLoading();
      wx.showToast({
        title: 'Failed to load',
        icon: 'none'
      });
    });
  }
});
