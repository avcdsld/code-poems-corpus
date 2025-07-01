public static boolean hasIndex(final Connection connection, final String tableName, final String indexName) throws SQLException {
        boolean hasIndex = false;
        
        ResultSet rs = null;
        try {
            rs = connection.getMetaData().getIndexInfo(null, null, tableName, false, false);
            while (rs.next()) {
            	if (indexName.equals(rs.getString("INDEX_NAME"))) {
            		hasIndex = true;
            		break;
            	}
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
        
        return hasIndex;
    }