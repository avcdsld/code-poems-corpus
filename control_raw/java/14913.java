@Override
  public Object extractPeerObject() throws GeneralSecurityException {
    Preconditions.checkState(!isInProgress(), "Handshake is not complete.");
    return new AltsAuthContext(handshaker.getResult());
  }