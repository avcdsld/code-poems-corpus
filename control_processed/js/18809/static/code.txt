function isOption(option) {
  if (!option || typeof option !== 'object') {
    return false;
  }

  let allOptions = Object.keys(defaultRouteOptions);
  let optionKeys = Object.keys(option);
  for (let i = 0; i < optionKeys.length; i++) {
    let key = optionKeys[i];
    if (allOptions.indexOf(key) > -1) {
      return true;
    }
  }
  return false;
}