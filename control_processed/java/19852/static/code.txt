public static byte[] concat(byte[]... arrays) {
		int size = 0;
		for (byte[] a: arrays) {
			size += a.length;
		}
		byte[] result = new byte[size];
		int index = 0;
		for (byte[] a: arrays) {
			System.arraycopy(a, 0, result, index, a.length);
			index += a.length;
		}
		return result;
	}