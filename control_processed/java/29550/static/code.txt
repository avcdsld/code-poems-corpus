public final ImportSshPublicKeyResponse importSshPublicKey(
      UserName parent, SshPublicKey sshPublicKey) {

    ImportSshPublicKeyRequest request =
        ImportSshPublicKeyRequest.newBuilder()
            .setParent(parent == null ? null : parent.toString())
            .setSshPublicKey(sshPublicKey)
            .build();
    return importSshPublicKey(request);
  }