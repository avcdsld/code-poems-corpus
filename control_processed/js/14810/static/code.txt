function crypt(fn, text, nonce, adata) {
    //
    // Consider P as a sequence of 128-bit blocks
    //
    const m = text.length / blockLength | 0;

    //
    // Key-dependent variables
    //
    extendKeyVariables(text, adata);

    //
    // Nonce-dependent and per-encryption variables
    //
    //    Nonce = num2str(TAGLEN mod 128,7) || zeros(120-bitlen(N)) || 1 || N
    // Note: We assume here that tagLength mod 16 == 0.
    const paddedNonce = util.concatUint8Array([zeroBlock.subarray(0, ivLength - nonce.length), one, nonce]);
    //    bottom = str2num(Nonce[123..128])
    const bottom = paddedNonce[blockLength - 1] & 0b111111;
    //    Ktop = ENCIPHER(K, Nonce[1..122] || zeros(6))
    paddedNonce[blockLength - 1] &= 0b11000000;
    const kTop = encipher(paddedNonce);
    //    Stretch = Ktop || (Ktop[1..64] xor Ktop[9..72])
    const stretched = util.concatUint8Array([kTop, xor(kTop.subarray(0, 8), kTop.subarray(1, 9))]);
    //    Offset_0 = Stretch[1+bottom..128+bottom]
    const offset = util.shiftRight(stretched.subarray(0 + (bottom >> 3), 17 + (bottom >> 3)), 8 - (bottom & 7)).subarray(1);
    //    Checksum_0 = zeros(128)
    const checksum = new Uint8Array(blockLength);

    const ct = new Uint8Array(text.length + tagLength);

    //
    // Process any whole blocks
    //
    let i;
    let pos = 0;
    for (i = 0; i < m; i++) {
      // Offset_i = Offset_{i-1} xor L_{ntz(i)}
      xorMut(offset, mask[ntz(i + 1)]);
      // C_i = Offset_i xor ENCIPHER(K, P_i xor Offset_i)
      // P_i = Offset_i xor DECIPHER(K, C_i xor Offset_i)
      ct.set(xorMut(fn(xor(offset, text)), offset), pos);
      // Checksum_i = Checksum_{i-1} xor P_i
      xorMut(checksum, fn === encipher ? text : ct.subarray(pos));

      text = text.subarray(blockLength);
      pos += blockLength;
    }

    //
    // Process any final partial block and compute raw tag
    //
    if (text.length) {
      // Offset_* = Offset_m xor L_*
      xorMut(offset, mask.x);
      // Pad = ENCIPHER(K, Offset_*)
      const padding = encipher(offset);
      // C_* = P_* xor Pad[1..bitlen(P_*)]
      ct.set(xor(text, padding), pos);

      // Checksum_* = Checksum_m xor (P_* || 1 || new Uint8Array(127-bitlen(P_*)))
      const xorInput = new Uint8Array(blockLength);
      xorInput.set(fn === encipher ? text : ct.subarray(pos, -tagLength), 0);
      xorInput[text.length] = 0b10000000;
      xorMut(checksum, xorInput);
      pos += text.length;
    }
    // Tag = ENCIPHER(K, Checksum_* xor Offset_* xor L_$) xor HASH(K,A)
    const tag = xorMut(encipher(xorMut(xorMut(checksum, offset), mask.$)), hash(adata));

    //
    // Assemble ciphertext
    //
    // C = C_1 || C_2 || ... || C_m || C_* || Tag[1..TAGLEN]
    ct.set(tag, pos);
    return ct;
  }