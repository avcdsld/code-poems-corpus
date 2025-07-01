@Override
	public void setValue(ELContext context, Object base, Object property, Object value) {
		if (context == null) {
			throw new NullPointerException("context is null");
		}
		if (base instanceof ObjectNode) {
			if (readOnly) {
				throw new PropertyNotWritableException("resolver is read-only");
			}
			ObjectNode node = (ObjectNode) base;
			if (value instanceof BigDecimal) {
				node.put(property.toString(), (BigDecimal) value);

			} else if (value instanceof Boolean) {
				node.put(property.toString(), (Boolean) value);

			} else if (value instanceof Long) {
				node.put(property.toString(), (Long) value);

			} else if (value instanceof Double) {
				node.put(property.toString(), (Double) value);

			} else if (value != null) {
				node.put(property.toString(), value.toString());

			} else {
				node.putNull(property.toString());
			}
			context.setPropertyResolved(true);
		}
	}