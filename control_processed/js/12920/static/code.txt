function(targetOptions, sourceOptions, keys, mergeWriteConcern) {
  // Mix in any allowed options
  for (var i = 0; i < keys.length; i++) {
    if (!targetOptions[keys[i]] && sourceOptions[keys[i]] !== undefined) {
      targetOptions[keys[i]] = sourceOptions[keys[i]];
    }
  }

  // No merging of write concern
  if (!mergeWriteConcern) return targetOptions;

  // Found no write Concern options
  var found = false;
  for (i = 0; i < writeConcernKeys.length; i++) {
    if (targetOptions[writeConcernKeys[i]]) {
      found = true;
      break;
    }
  }

  if (!found) {
    for (i = 0; i < writeConcernKeys.length; i++) {
      if (sourceOptions[writeConcernKeys[i]]) {
        targetOptions[writeConcernKeys[i]] = sourceOptions[writeConcernKeys[i]];
      }
    }
  }

  return targetOptions;
}