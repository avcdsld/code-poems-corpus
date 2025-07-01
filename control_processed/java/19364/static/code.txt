public static String buildGlueExpression(List<Column> partitionKeys, List<String> partitionValues)
    {
        if (partitionValues == null || partitionValues.isEmpty()) {
            return null;
        }

        if (partitionKeys == null || partitionValues.size() != partitionKeys.size()) {
            throw new PrestoException(HIVE_METASTORE_ERROR, "Incorrect number of partition values: " + partitionValues);
        }

        List<String> predicates = new LinkedList<>();
        for (int i = 0; i < partitionValues.size(); i++) {
            if (!Strings.isNullOrEmpty(partitionValues.get(i))) {
                predicates.add(buildPredicate(partitionKeys.get(i), partitionValues.get(i)));
            }
        }

        return JOINER.join(predicates);
    }