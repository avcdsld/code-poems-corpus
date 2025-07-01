function() {
    _detectSandbox();
    return {
      browser: _extend(_pick(_navigator, [ "userAgent", "platform", "appName", "appVersion" ]), {
        isSupported: _isBrowserSupported()
      }),
      flash: _omit(_flashState, [ "bridge" ]),
      zeroclipboard: {
        version: ZeroClipboard.version,
        config: ZeroClipboard.config()
      }
    };
  }