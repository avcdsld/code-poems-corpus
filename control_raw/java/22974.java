public static String toGetterName(AST<?, ?, ?> ast, AnnotationValues<Accessors> accessors, CharSequence fieldName, boolean isBoolean) {
		return toAccessorName(ast, accessors, fieldName, isBoolean, "is", "get", true);
	}