function getCurrentActiveType (version) {
  let typelist = TypeList
  for (let i = 0; i < typelist.length; i++) {
    if (semver[typelist[i]](version)) {
      return typelist[i]
    }
  }
}