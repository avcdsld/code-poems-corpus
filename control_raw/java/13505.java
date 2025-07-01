public Map<String, AttributeValue> buildTableAttributeValuesMapFromService(final RegisteredService service) {
        val values = new HashMap<String, AttributeValue>();
        values.put(ColumnNames.ID.getColumnName(), new AttributeValue(String.valueOf(service.getId())));
        values.put(ColumnNames.NAME.getColumnName(), new AttributeValue(service.getName()));
        values.put(ColumnNames.DESCRIPTION.getColumnName(), new AttributeValue(service.getDescription()));
        values.put(ColumnNames.SERVICE_ID.getColumnName(), new AttributeValue(service.getServiceId()));
        val out = new ByteArrayOutputStream();
        jsonSerializer.to(out, service);
        values.put(ColumnNames.ENCODED.getColumnName(), new AttributeValue().withB(ByteBuffer.wrap(out.toByteArray())));
        LOGGER.debug("Created attribute values [{}] based on provided service [{}]", values, service);
        return values;
    }