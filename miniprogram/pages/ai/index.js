const api = require("../../utils/api.js");
const app = getApp();

Page({
  data: {
    movies: [],
    inputValue: "",
    loading: false,
    imageBaseUrl: "https://image.tmdb.org/t/p/w200",
    statusBarHeight: 0,
    navBarHeight: 44,
    totalNavHeight: 64,

    // Typing animation
    fullText: "告诉我你今天想看什么...",
    candidateTexts: [
      "告诉我你今天想看什么...",
      "关于时间旅行的科幻片",
      "90年代的搞笑电影",
      "获奖的剧情片",
    ],
    typedText: "",
    cursorVisible: true,
  },
  onLoad() {
    this.setData({
      statusBarHeight: app.globalData.statusBarHeight,
      navBarHeight: app.globalData.navBarHeight,
      totalNavHeight: app.globalData.totalNavHeight,
    });
    this.startTypingAnimation();
  },

  startTypingAnimation() {
    const texts = this.data.candidateTexts;
    let textIndex = 0;
    let charIndex = 0;
    let isDeleting = false;
    let typingSpeed = 100;

    const type = () => {
      const currentFullText = texts[textIndex];

      if (isDeleting) {
        this.setData({
          typedText: currentFullText.substring(0, charIndex - 1),
        });
        charIndex--;
        typingSpeed = 50; // Deleting speed
      } else {
        this.setData({
          typedText: currentFullText.substring(0, charIndex + 1),
        });
        charIndex++;
        typingSpeed = 100; // Typing speed
      }

      // Cursor blinking effect during typing
      this.setData({ cursorVisible: true });

      if (!isDeleting && charIndex === currentFullText.length) {
        // Finished typing
        isDeleting = true;
        typingSpeed = 2000; // Pause at end
      } else if (isDeleting && charIndex === 0) {
        // Finished deleting
        isDeleting = false;
        textIndex = (textIndex + 1) % texts.length;
        typingSpeed = 500; // Pause before new text
      }

      this.typingTimer = setTimeout(type, typingSpeed);
    };

    type();

    // Separate cursor blinking interval
    this.cursorInterval = setInterval(() => {
      this.setData({ cursorVisible: !this.data.cursorVisible });
    }, 500);
  },

  onUnload() {
    if (this.cursorInterval) {
      clearInterval(this.cursorInterval);
    }
    if (this.typingTimer) {
      clearTimeout(this.typingTimer);
    }
  },
  onInput(e) {
    this.setData({ inputValue: e.detail.value });
  },
  onSend() {
    const prompt = this.data.inputValue.trim();
    if (!prompt) return;

    this.setData({ loading: true, movies: [] });

    api
      .getAIRecommendation(prompt)
      .then((res) => {
        this.setData({
          movies: res.movies || [],
          loading: false,
        });
      })
      .catch((err) => {
        console.error(err);
        this.setData({ loading: false });
        wx.showToast({
          title: "推荐失败",
          icon: "none",
        });
      });
  },
  goToDetail(e) {
    const id = e.currentTarget.dataset.id;
    wx.navigateTo({
      url: `/pages/detail/detail?id=${id}`,
    });
  },
});
