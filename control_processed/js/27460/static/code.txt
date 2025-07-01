function() {
    var lvldownObj = target.apply(null, arguments);
    lvldownObj._ddProbeAttached_ = true;
    aspectLvldownMethod(lvldownObj, methods, that);
    return lvldownObj;
  }