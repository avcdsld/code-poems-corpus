function sendRequest(type, options) {
    // Both remove and removeAll use the type 'remove' in the protocol
    const normalizedType = type === 'removeAll' ? 'remove' : type
    return socket
      .hzRequest({ type: normalizedType, options }) // send the raw request
      .takeWhile(resp => resp.state !== 'complete')
  }