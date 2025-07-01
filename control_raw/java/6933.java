public static int pjwHash(String str) {
		int bitsInUnsignedInt = 32;
		int threeQuarters = (bitsInUnsignedInt * 3) / 4;
		int oneEighth = bitsInUnsignedInt / 8;
		int highBits = 0xFFFFFFFF << (bitsInUnsignedInt - oneEighth);
		int hash = 0;
		int test = 0;

		for (int i = 0; i < str.length(); i++) {
			hash = (hash << oneEighth) + str.charAt(i);

			if ((test = hash & highBits) != 0) {
				hash = ((hash ^ (test >> threeQuarters)) & (~highBits));
			}
		}

		return hash & 0x7FFFFFFF;
	}