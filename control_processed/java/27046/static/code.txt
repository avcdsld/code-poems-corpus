public static String queryBank(Map<String, String> params, String certPath, String certPassword) {
		return WxPayApi.doPostSSL(QUERY_BANK_URL, params, certPath, certPassword);
	}