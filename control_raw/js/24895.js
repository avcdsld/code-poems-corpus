function keyuri(user = 'user', service = 'service', secret = '') {
  const protocol = 'otpauth://totp/';
  const value = data
    .replace('{user}', encodeURIComponent(user))
    .replace('{secret}', secret)
    .replace(/{service}/g, encodeURIComponent(service));

  return protocol + value;
}