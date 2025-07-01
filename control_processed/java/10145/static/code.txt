public final void setColumnValue(final String columnName, final Object columnValue) {
        SQLExpression sqlExpression = values[getColumnIndex(columnName)];
        if (sqlExpression instanceof SQLParameterMarkerExpression) {
            parameters[getParameterIndex(sqlExpression)] = columnValue;
        } else {
            SQLExpression columnExpression = String.class == columnValue.getClass() ? new SQLTextExpression(String.valueOf(columnValue)) : new SQLNumberExpression((Number) columnValue);
            values[getColumnIndex(columnName)] = columnExpression;
        }
    }