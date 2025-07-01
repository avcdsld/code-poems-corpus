function encrypt(key, kdfParams) {
    var uuid = kdfParams.get('$UUID');
    if (!uuid || !(uuid instanceof ArrayBuffer)) {
        return Promise.reject(new KdbxError(Consts.ErrorCodes.FileCorrupt, 'no kdf uuid'));
    }
    var kdfUuid = ByteUtils.bytesToBase64(uuid);
    switch (kdfUuid) {
        case Consts.KdfId.Argon2:
            return encryptArgon2(key, kdfParams);
        case Consts.KdfId.Aes:
            return encryptAes(key, kdfParams);
        default:
            return Promise.reject(new KdbxError(Consts.ErrorCodes.Unsupported, 'bad kdf'));
    }
}