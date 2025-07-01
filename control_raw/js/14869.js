async function webGenKeyPair(name) {
  // Note: keys generated with ECDSA and ECDH are structurally equivalent
  const webCryptoKey = await webCrypto.generateKey({ name: "ECDSA", namedCurve: webCurves[name] }, true, ["sign", "verify"]);

  const privateKey = await webCrypto.exportKey("jwk", webCryptoKey.privateKey);
  const publicKey = await webCrypto.exportKey("jwk", webCryptoKey.publicKey);

  return {
    pub: {
      x: util.b64_to_Uint8Array(publicKey.x, true),
      y: util.b64_to_Uint8Array(publicKey.y, true)
    },
    priv: util.b64_to_Uint8Array(privateKey.d, true)
  };
}