public static void init(String sensitiveWords, char separator, boolean isAsync){
		if(StrUtil.isNotBlank(sensitiveWords)){
			init(StrUtil.split(sensitiveWords, separator), isAsync);
		}
	}