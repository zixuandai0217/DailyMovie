App({
  onLaunch() {
    console.log("App Launch");
    // Get system info for custom navigation bar
    const sysInfo = wx.getSystemInfoSync();
    this.globalData.statusBarHeight = sysInfo.statusBarHeight;
    // Standard navigation bar height is usually 44px on iOS and 48px on Android, but 44px is a safe default for custom implementations
    this.globalData.navBarHeight = 44;
    this.globalData.totalNavHeight = sysInfo.statusBarHeight + 44;
  },
  globalData: {
    userInfo: null,
    statusBarHeight: 0,
    navBarHeight: 44,
    totalNavHeight: 0,
  },
});
