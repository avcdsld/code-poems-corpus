function softwareUpdate() {
  this._controller = null;
  this._wizard = null;

  this._aus = Cc["@mozilla.org/updates/update-service;1"].
              getService(Ci.nsIApplicationUpdateService);
  this._ums = Cc["@mozilla.org/updates/update-manager;1"].
              getService(Ci.nsIUpdateManager);
  this._vc = Cc["@mozilla.org/xpcom/version-comparator;1"].
             getService(Ci.nsIVersionComparator);
}