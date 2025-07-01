function isSameToken(token1, token2) {
  if (isValidToken(token1) && isValidToken(token2)) {
    return String(token1) === String(token2);
  }

  return false;
}