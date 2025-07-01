public static void validateBetween(Number value, Number min, Number max, String errorMsg) throws ValidateException {
		if (false == isBetween(value, min, max)) {
			throw new ValidateException(errorMsg);
		}
	}