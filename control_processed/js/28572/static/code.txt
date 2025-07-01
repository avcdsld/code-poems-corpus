function registerFilters (filters) {
  if (isArray(filters)) {
    lazyStringFilters = lazyStringFilters.concat(filters)
  } else if (isObject(filters)) {
    Object.keys(filters).forEach(name => {
      addFilter(name, filters[name])
    })
  }
}