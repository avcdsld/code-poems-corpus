function getIpPath(req) {
  const output = [];

  const realIpHeader = req.headers['x-real-ip'];
  if (realIpHeader) {
    output.push('Real:');
    output.push(realIpHeader);
    output.push(' ');
  }

  const forwardedForHeader = req.headers['x-forwarded-for'];
  if (forwardedForHeader) {
    output.push('ForwardedFor:');
    output.push(forwardedForHeader);
    output.push(' ');
  }

  if (req.connection.remoteAddress !== '127.0.0.1') {
    output.push('remoteIp: ');
    output.push(req.connection.remoteAddress);
  }

  return output.join('');
}