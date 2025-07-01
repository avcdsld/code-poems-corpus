private static List<FieldItem> collectSelectQueryFields(MySqlSelectQueryBlock sqlSelectQueryBlock) {
        return sqlSelectQueryBlock.getSelectList().stream().map(selectItem -> {
            FieldItem fieldItem = new FieldItem();
            fieldItem.setFieldName(selectItem.getAlias());
            fieldItem.setExpr(selectItem.toString());
            visitColumn(selectItem.getExpr(), fieldItem);
            return fieldItem;
        }).collect(Collectors.toList());
    }