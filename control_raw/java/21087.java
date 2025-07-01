public static int getColumnType(final Connection connection, final String tableName, final String columnName) throws SQLException {
        int columnType = -1;
        
        ResultSet rs = null;
        try {
            rs = connection.getMetaData().getColumns(null, null, tableName, columnName);
            if (rs.next()) {
                columnType = rs.getInt("SQL_DATA_TYPE");
            }
        } finally {
            try {
                if (rs != null) {
                    rs.close();
                }
            } catch (SQLException e) {
                if (logger.isDebugEnabled()) {
                    logger.debug(e.getMessage(), e);
                }
            }
        }
        
        return columnType;
    }