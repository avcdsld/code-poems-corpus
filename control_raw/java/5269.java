public static TypeInformation<Row> ROW_NAMED(String[] fieldNames, TypeInformation<?>... types) {
		return new RowTypeInfo(types, fieldNames);
	}