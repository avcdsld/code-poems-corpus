function isForwardByArray (to, from) {
  // 根据 fullPath 判断当前页面是否访问过，如果访问过，则属于返回

  let index = HISTORY_STACK.indexOf(to.fullPath)
  if (index !== -1) {
    HISTORY_STACK.length = index + 1
    return false
  }

  return true
}