public static String buildLikeValue(String value, LikeType likeType, boolean withLikeKeyword) {
		if (null == value) {
			return value;
		}

		StringBuilder likeValue = StrUtil.builder(withLikeKeyword ? "LIKE " : "");
		switch (likeType) {
		case StartWith:
			likeValue.append('%').append(value);
			break;
		case EndWith:
			likeValue.append(value).append('%');
			break;
		case Contains:
			likeValue.append('%').append(value).append('%');
			break;

		default:
			break;
		}
		return likeValue.toString();
	}