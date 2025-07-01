async function EAX(cipher, key) {
  if (cipher.substr(0, 3) !== 'aes') {
    throw new Error('EAX mode supports only AES cipher');
  }

  const [
    omac,
    ctr
  ] = await Promise.all([
    OMAC(key),
    CTR(key)
  ]);

  return {
    /**
     * Encrypt plaintext input.
     * @param  {Uint8Array} plaintext   The cleartext input to be encrypted
     * @param  {Uint8Array} nonce       The nonce (16 bytes)
     * @param  {Uint8Array} adata       Associated data to sign
     * @returns {Promise<Uint8Array>}    The ciphertext output
     */
    encrypt: async function(plaintext, nonce, adata) {
      const [
        omacNonce,
        omacAdata
      ] = await Promise.all([
        omac(zero, nonce),
        omac(one, adata)
      ]);
      const ciphered = await ctr(plaintext, omacNonce);
      const omacCiphered = await omac(two, ciphered);
      const tag = omacCiphered; // Assumes that omac(*).length === tagLength.
      for (let i = 0; i < tagLength; i++) {
        tag[i] ^= omacAdata[i] ^ omacNonce[i];
      }
      return util.concatUint8Array([ciphered, tag]);
    },

    /**
     * Decrypt ciphertext input.
     * @param  {Uint8Array} ciphertext   The ciphertext input to be decrypted
     * @param  {Uint8Array} nonce        The nonce (16 bytes)
     * @param  {Uint8Array} adata        Associated data to verify
     * @returns {Promise<Uint8Array>}     The plaintext output
     */
    decrypt: async function(ciphertext, nonce, adata) {
      if (ciphertext.length < tagLength) throw new Error('Invalid EAX ciphertext');
      const ciphered = ciphertext.subarray(0, -tagLength);
      const ctTag = ciphertext.subarray(-tagLength);
      const [
        omacNonce,
        omacAdata,
        omacCiphered
      ] = await Promise.all([
        omac(zero, nonce),
        omac(one, adata),
        omac(two, ciphered)
      ]);
      const tag = omacCiphered; // Assumes that omac(*).length === tagLength.
      for (let i = 0; i < tagLength; i++) {
        tag[i] ^= omacAdata[i] ^ omacNonce[i];
      }
      if (!util.equalsUint8Array(ctTag, tag)) throw new Error('Authentication tag mismatch');
      const plaintext = await ctr(ciphered, omacNonce);
      return plaintext;
    }
  };
}