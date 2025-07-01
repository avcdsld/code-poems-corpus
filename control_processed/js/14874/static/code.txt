async function genPublicEphemeralKey(curve, Q) {
  if (curve.name === 'curve25519') {
    const { secretKey: d } = nacl.box.keyPair();
    const { secretKey, sharedKey } = await genPrivateEphemeralKey(curve, Q, d);
    let { publicKey } = nacl.box.keyPair.fromSecretKey(secretKey);
    publicKey = util.concatUint8Array([new Uint8Array([0x40]), publicKey]);
    return { publicKey, sharedKey }; // Note: sharedKey is little-endian here, unlike below
  }
  const v = await curve.genKeyPair();
  Q = curve.keyFromPublic(Q);
  const publicKey = new Uint8Array(v.getPublic());
  const S = v.derive(Q);
  const len = curve.curve.curve.p.byteLength();
  const sharedKey = S.toArrayLike(Uint8Array, 'be', len);
  return { publicKey, sharedKey };
}