function trailingEdge(time) {
    timerId = undefined;
    // 有lastArgs才执行，
    // 意味着只有 func 已经被 debounced 过一次以后才会在 trailing edge 执行
    if (trailing && lastArgs) {
      return invokeFunc(time);
    }
    // 每次 trailingEdge 都会清除 lastArgs 和 lastThis，目的是避免最后一次函数被执行了两次
    // 举个例子：最后一次函数执行的时候，可能恰巧是前一次的 trailing edge，函数被调用，而这个函数又需要在自己时延的 trailing edge 触发，导致触发多次
    lastArgs = lastThis = undefined;
    return result;
  }