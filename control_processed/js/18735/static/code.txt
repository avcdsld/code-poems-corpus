function buildXOAuth2Token(user = '', token) {
  let authData = [`user=${user}`, `auth=Bearer ${token}`, '', ''];
  return (0, _emailjsBase.encode)(authData.join('\x01'));
}