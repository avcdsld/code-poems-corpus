function arraybuffer2packed(arr, existingPacked, existingPackedLen, bigEndianMod)
	{
		var packed, i, existingByteLen, intOffset, byteOffset, shiftModifier, arrView;

		packed = existingPacked || [0];
		existingPackedLen = existingPackedLen || 0;
		existingByteLen = existingPackedLen >>> 3;
		shiftModifier = (bigEndianMod === -1) ? 3 : 0;
		arrView = new Uint8Array(arr);

		for (i = 0; i < arr.byteLength; i += 1)
		{
			byteOffset = i + existingByteLen;
			intOffset = byteOffset >>> 2;
			if (packed.length <= intOffset)
			{
				packed.push(0);
			}
			packed[intOffset] |= arrView[i] << (8 * (shiftModifier + bigEndianMod * (byteOffset % 4)));
		}

		return {"value" : packed, "binLen" : arr.byteLength * 8 + existingPackedLen};
	}