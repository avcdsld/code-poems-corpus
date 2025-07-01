public <V> V executeScalar(Class<V> returnType) {
        try (ResultSet rs = executeQuery()) {
            if (!rs.next()) {
                Object value = null;
                if (Integer.class == returnType) {
                    value = 0;
                } else if (Long.class == returnType) {
                    value = 0L;
                } else if (Boolean.class == returnType) {
                    value = false;
                }
                return returnType.cast(value);
            } else {
                return getScalarFromResultSet(rs, returnType);
            }
        } catch (SQLException ex) {
            throw new ApplicationException(Code.BACKEND_ERROR, ex);
        }
    }