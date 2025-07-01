function(event) {
    var eventType;
    if (typeof event === "string" && event) {
      eventType = event;
      event = {};
    } else if (typeof event === "object" && event && typeof event.type === "string" && event.type) {
      eventType = event.type;
    }
    if (!eventType) {
      return;
    }
    eventType = eventType.toLowerCase();
    if (!event.target && (/^(copy|aftercopy|_click)$/.test(eventType) || eventType === "error" && event.name === "clipboard-error")) {
      event.target = _copyTarget;
    }
    _extend(event, {
      type: eventType,
      target: event.target || _currentElement || null,
      relatedTarget: event.relatedTarget || null,
      currentTarget: _flashState && _flashState.bridge || null,
      timeStamp: event.timeStamp || _now() || null
    });
    var msg = _eventMessages[event.type];
    if (event.type === "error" && event.name && msg) {
      msg = msg[event.name];
    }
    if (msg) {
      event.message = msg;
    }
    if (event.type === "ready") {
      _extend(event, {
        target: null,
        version: _flashState.version
      });
    }
    if (event.type === "error") {
      if (_flashStateErrorNameMatchingRegex.test(event.name)) {
        _extend(event, {
          target: null,
          minimumVersion: _minimumFlashVersion
        });
      }
      if (_flashStateEnabledErrorNameMatchingRegex.test(event.name)) {
        _extend(event, {
          version: _flashState.version
        });
      }
      if (event.name === "flash-insecure") {
        _extend(event, {
          pageProtocol: _window.location.protocol,
          swfProtocol: _getSwfPathProtocol()
        });
      }
    }
    if (event.type === "copy") {
      event.clipboardData = {
        setData: ZeroClipboard.setData,
        clearData: ZeroClipboard.clearData
      };
    }
    if (event.type === "aftercopy") {
      event = _mapClipResultsFromFlash(event, _clipDataFormatMap);
    }
    if (event.target && !event.relatedTarget) {
      event.relatedTarget = _getRelatedTarget(event.target);
    }
    return _addMouseData(event);
  }