// 开发环境使用局域网 IP，注意同时要在微信开发者工具中开启"不校验合法域名"
const BASE_URL = "http://192.168.31.62:8000/api/v1";

const request = (url, method = "GET", data = {}, header = {}) => {
  return new Promise((resolve, reject) => {
    wx.request({
      url: `${BASE_URL}${url}`,
      method: method,
      data: data,
      header: {
        "content-type": "application/json",
        ...header,
      },
      success(res) {
        if (res.statusCode >= 200 && res.statusCode < 300) {
          resolve(res.data);
        } else {
          reject(res);
        }
      },
      fail(err) {
        reject(err);
      },
    });
  });
};

module.exports = {
  getRandomMovie: () => request("/movies/random"),
  searchMovies: (query) => request("/movies/search", "GET", { query }),
  getMovieDetail: (id) => request(`/movies/${id}`),

  // User & Auth
  login: (code, userInfo) => request("/user/login", "POST", { code, userInfo }),
  getProfile: (token) => request(`/user/profile?token=${token}`),
  updatePreferences: (token, prefs) =>
    request(`/user/preferences?token=${token}`, "PUT", prefs),

  // AI
  getAIRecommendation: (prompt) => request("/ai/recommend", "POST", { prompt }),
};
