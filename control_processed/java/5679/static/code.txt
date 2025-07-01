public static int bitMix(int in) {
		in ^= in >>> 16;
		in *= 0x85ebca6b;
		in ^= in >>> 13;
		in *= 0xc2b2ae35;
		in ^= in >>> 16;
		return in;
	}