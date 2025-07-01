async function webSign(curve, hash_algo, message, keyPair) {
  const len = curve.payloadSize;
  const key = await webCrypto.importKey(
    "jwk",
    {
      "kty": "EC",
      "crv": webCurves[curve.name],
      "x": util.Uint8Array_to_b64(new Uint8Array(keyPair.getPublic().getX().toArray('be', len)), true),
      "y": util.Uint8Array_to_b64(new Uint8Array(keyPair.getPublic().getY().toArray('be', len)), true),
      "d": util.Uint8Array_to_b64(new Uint8Array(keyPair.getPrivate().toArray('be', len)), true),
      "use": "sig",
      "kid": "ECDSA Private Key"
    },
    {
      "name": "ECDSA",
      "namedCurve": webCurves[curve.name],
      "hash": { name: enums.read(enums.webHash, curve.hash) }
    },
    false,
    ["sign"]
  );

  const signature = new Uint8Array(await webCrypto.sign(
    {
      "name": 'ECDSA',
      "namedCurve": webCurves[curve.name],
      "hash": { name: enums.read(enums.webHash, hash_algo) }
    },
    key,
    message
  ));

  return {
    r: new BN(signature.slice(0, len)),
    s: new BN(signature.slice(len, len << 1))
  };
}