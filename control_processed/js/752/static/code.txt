function addonsManager_getAddonLink(aSpec) {
    var spec = aSpec || { };
    var addon = spec.addon;
    var link = spec.link;

    if (!link)
      throw new Error(arguments.callee.name + ": Link not specified.");

    return this.getAddonChildElement({addon: addon, type: link + "Link"});
  }