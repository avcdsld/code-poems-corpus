public static boolean isPrimes(int n) {
		Assert.isTrue(n > 1, "The number must be > 1");
		for (int i = 2; i <= Math.sqrt(n); i++) {
			if (n % i == 0) {
				return false;
			}
		}
		return true;
	}