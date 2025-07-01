public static String sqlValueToString(ResultSet rs, int index, int sqlType) throws SQLException {
        Class<?> requiredType = sqlTypeToJavaTypeMap.get(sqlType);
        if (requiredType == null) {
            throw new IllegalArgumentException("unknow java.sql.Types - " + sqlType);
        }

        return getResultSetValue(rs, index, requiredType);
    }