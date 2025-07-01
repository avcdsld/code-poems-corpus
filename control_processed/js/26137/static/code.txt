function customizeProperties(mixinDetails, propertyInfo) {
  let newMixinDetails = [];
  let neededProperties = {};
  let groups = propertyInfo.groups || [];
  let skipProperties = propertyInfo.skipProperties || [];
  let skipMixins = propertyInfo.skipMixins || [];

  if (groups.length) {
    mixinDetails[0].expand = false;
  }

  groups.forEach(group => {
    group.properties.forEach(prop => {
      neededProperties[prop] = true;
    });
  });

  mixinDetails.forEach(mixin => {
    let newProperties = [];
    mixin.properties.forEach(item => {
      // If 2.10.0 or 2.10.x but < 2.11
      if (compareVersion(VERSION, '2.10.0') === 0 ||
        (compareVersion(VERSION, '2.10.0') === 1 && compareVersion(VERSION, '2.11.0') === -1)) {
        skipProperties = twoTenfilterHack(item.name, skipProperties);
      }
      if (skipProperties.indexOf(item.name) !== -1) {
        return true;
      }

      if (!item.overridden && neededProperties.hasOwnProperty(item.name) && neededProperties[item.name]) {
        neededProperties[item.name] = item;
      } else {
        newProperties.push(item);
      }
    });
    mixin.properties = newProperties;
    if (skipMixins.indexOf(mixin.name) === -1) {
      newMixinDetails.push(mixin);
    }
  });

  groups.slice().reverse().forEach(group => {
    let newMixin = { name: group.name, expand: group.expand, properties: [] };
    group.properties.forEach(function(prop) {
      // make sure it's not `true` which means property wasn't found
      if (neededProperties[prop] !== true) {
        newMixin.properties.push(neededProperties[prop]);
      }
    });
    newMixinDetails.unshift(newMixin);
  });

  return newMixinDetails;
}