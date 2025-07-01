public static String intToIpv4String(int i) {
		return new StringBuilder(15).append((i >> 24) & 0xff).append('.').append((i >> 16) & 0xff).append('.')
				.append((i >> 8) & 0xff).append('.').append(i & 0xff).toString();
	}