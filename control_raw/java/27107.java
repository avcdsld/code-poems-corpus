public static String buildRequestMysign(Map<String, String> params, String key, String signType) {
		String prestr = createLinkString(params); // 把数组所有元素，按照“参数=参数值”的模式用“&”字符拼接成字符串
		if (signType.equals("MD5")) {
			return HashKit.md5(prestr.concat(key));
		}
		return null;
	}