function keyboardGetHeight() {
  // check if we already have a keyboard height from the plugin or resize calculations
  if (ionic.keyboard.height) {
    return ionic.keyboard.height;
  }

  if (ionic.Platform.isAndroid()) {
    // should be using the plugin, no way to know how big the keyboard is, so guess
    if ( ionic.Platform.isFullScreen ) {
      return 275;
    }
    // otherwise just calculate it
    var contentHeight = window.innerHeight;
    if (contentHeight < keyboardCurrentViewportHeight) {
      return keyboardCurrentViewportHeight - contentHeight;
    } else {
      return 0;
    }
  }

  // fallback for when it's the webview without the plugin
  // or for just the standard web browser
  // TODO: have these be based on device
  if (ionic.Platform.isIOS()) {
    if (ionic.keyboard.isLandscape) {
      return 206;
    }

    if (!ionic.Platform.isWebView()) {
      return 216;
    }

    return 260;
  }

  // safe guess
  return 275;
}