function dropPromise (target) {
  let index = mipDataPromises.indexOf(target)
  mipDataPromises.splice(index, ~index ? 1 : 0)
}