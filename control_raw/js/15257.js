function verifyAndDecrypt(key,nonce,ciphertext,mac,addData,plaintext) {
  var ctx = new chacha20poly1305.Chacha20Ctx();
  chacha20poly1305.chacha20_keysetup(ctx, key);
  chacha20poly1305.chacha20_ivsetup(ctx, nonce);
  var poly1305key = bufferShim.alloc(64);
  var zeros = bufferShim.alloc(64);
  chacha20poly1305.chacha20_update(ctx,poly1305key,zeros,zeros.length);

  var poly1305_contxt = new chacha20poly1305.Poly1305Ctx();
  chacha20poly1305.poly1305_init(poly1305_contxt, poly1305key);

  var addDataLength = 0;
  if (addData != undefined) {
    addDataLength = addData.length;
    chacha20poly1305.poly1305_update(poly1305_contxt, addData, addData.length);
    if ((addData.length % 16) != 0) {
      chacha20poly1305.poly1305_update(poly1305_contxt, bufferShim.alloc(16-(addData.length%16)), 16-(addData.length%16));
    }
  }

  chacha20poly1305.poly1305_update(poly1305_contxt, ciphertext, ciphertext.length);
  if ((ciphertext.length % 16) != 0) {
    chacha20poly1305.poly1305_update(poly1305_contxt, bufferShim.alloc(16-(ciphertext.length%16)), 16-(ciphertext.length%16));
  }

  var leAddDataLen = bufferShim.alloc(8);
  writeUInt64LE(addDataLength, leAddDataLen, 0);
  chacha20poly1305.poly1305_update(poly1305_contxt, leAddDataLen, 8);

  var leTextDataLen = bufferShim.alloc(8);
  writeUInt64LE(ciphertext.length, leTextDataLen, 0);
  chacha20poly1305.poly1305_update(poly1305_contxt, leTextDataLen, 8);

  var poly_out = [];
  chacha20poly1305.poly1305_finish(poly1305_contxt, poly_out);

  if (chacha20poly1305.poly1305_verify(mac, poly_out) != 1) {
    debug('Verify Fail');
    return false;
  } else {
    var written = chacha20poly1305.chacha20_update(ctx,plaintext,ciphertext,ciphertext.length);
    chacha20poly1305.chacha20_final(ctx,plaintext.slice(written, ciphertext.length));
    return true;
  }
}