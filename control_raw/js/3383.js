function shouldInvoke(time) {
    let timeSinceLastCall = time - lastCallTime;

    let timeSinceLastInvoke = time - lastInvokeTime;
    // 几种满足条件的情况
    return (lastCallTime === undefined ||
      (timeSinceLastCall >= wait) ||
      (timeSinceLastCall < 0) ||
      (maxing && timeSinceLastInvoke >= maxWait)); // 超过最大等待时间
  }