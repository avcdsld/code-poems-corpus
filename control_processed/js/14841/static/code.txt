async function GCM(cipher, key) {
  if (cipher.substr(0, 3) !== 'aes') {
    throw new Error('GCM mode supports only AES cipher');
  }

  if (util.getWebCrypto() && key.length !== 24) { // WebCrypto (no 192 bit support) see: https://www.chromium.org/blink/webcrypto#TOC-AES-support
    const _key = await webCrypto.importKey('raw', key, { name: ALGO }, false, ['encrypt', 'decrypt']);

    return {
      encrypt: async function(pt, iv, adata=new Uint8Array()) {
        if (
          !pt.length ||
          // iOS does not support GCM-en/decrypting empty messages
          // Also, synchronous en/decryption might be faster in this case.
          (!adata.length && navigator.userAgent.indexOf('Edge') !== -1)
          // Edge does not support GCM-en/decrypting without ADATA
        ) {
          return AES_GCM.encrypt(pt, key, iv, adata);
        }
        const ct = await webCrypto.encrypt({ name: ALGO, iv, additionalData: adata, tagLength: tagLength * 8 }, _key, pt);
        return new Uint8Array(ct);
      },

      decrypt: async function(ct, iv, adata=new Uint8Array()) {
        if (
          ct.length === tagLength ||
          // iOS does not support GCM-en/decrypting empty messages
          // Also, synchronous en/decryption might be faster in this case.
          (!adata.length && navigator.userAgent.indexOf('Edge') !== -1)
          // Edge does not support GCM-en/decrypting without ADATA
        ) {
          return AES_GCM.decrypt(ct, key, iv, adata);
        }
        const pt = await webCrypto.decrypt({ name: ALGO, iv, additionalData: adata, tagLength: tagLength * 8 }, _key, ct);
        return new Uint8Array(pt);
      }
    };
  }

  if (util.getNodeCrypto()) { // Node crypto library
    key = new Buffer(key);

    return {
      encrypt: async function(pt, iv, adata=new Uint8Array()) {
        pt = new Buffer(pt);
        iv = new Buffer(iv);
        adata = new Buffer(adata);
        const en = new nodeCrypto.createCipheriv('aes-' + (key.length * 8) + '-gcm', key, iv);
        en.setAAD(adata);
        const ct = Buffer.concat([en.update(pt), en.final(), en.getAuthTag()]); // append auth tag to ciphertext
        return new Uint8Array(ct);
      },

      decrypt: async function(ct, iv, adata=new Uint8Array()) {
        ct = new Buffer(ct);
        iv = new Buffer(iv);
        adata = new Buffer(adata);
        const de = new nodeCrypto.createDecipheriv('aes-' + (key.length * 8) + '-gcm', key, iv);
        de.setAAD(adata);
        de.setAuthTag(ct.slice(ct.length - tagLength, ct.length)); // read auth tag at end of ciphertext
        const pt = Buffer.concat([de.update(ct.slice(0, ct.length - tagLength)), de.final()]);
        return new Uint8Array(pt);
      }
    };
  }

  return {
    encrypt: async function(pt, iv, adata) {
      return AES_GCM.encrypt(pt, key, iv, adata);
    },

    decrypt: async function(ct, iv, adata) {
      return AES_GCM.decrypt(ct, key, iv, adata);
    }
  };
}