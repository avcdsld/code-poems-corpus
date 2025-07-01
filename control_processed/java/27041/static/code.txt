public static String downloadBill(boolean isSandbox, Map<String, String> params) {
		if (isSandbox)
			return doPost(DOWNLOADBILLY_SANDBOXNEW_URL, params);
		return doPost(DOWNLOADBILLY_URL, params);
	}