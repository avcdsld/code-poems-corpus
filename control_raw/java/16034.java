private void appendWhereIdList(StringBuilder sql, Class<?> entityClass, boolean notEmpty){
        Set<EntityColumn> columnList = EntityHelper.getPKColumns(entityClass);
        if (columnList.size() == 1) {
            EntityColumn column = columnList.iterator().next();
            if(notEmpty){
                sql.append("<bind name=\"notEmptyListCheck\" value=\"@tk.mybatis.mapper.additional.idlist.IdListProvider@notEmpty(");
                sql.append("idList, 'idList 不能为空')\"/>");
            }
            sql.append("<where>");
            sql.append("<foreach collection=\"idList\" item=\"id\" separator=\",\" open=\"");
            sql.append(column.getColumn());
            sql.append(" in ");
            sql.append("(\" close=\")\">");
            sql.append("#{id}");
            sql.append("</foreach>");
            sql.append("</where>");
        } else {
            throw new MapperException("继承 ByIdList 方法的实体类[" + entityClass.getCanonicalName() + "]中必须只有一个带有 @Id 注解的字段");
        }
    }