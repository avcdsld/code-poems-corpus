private int convertToInt(Object o, int defaultValue) {
		if (o.getClass() == Integer.class) {
			return (Integer) o;
		}
		else if (o.getClass() == Long.class) {
			long value = (Long) o;
			if (value <= Integer.MAX_VALUE && value >= Integer.MIN_VALUE) {
				return (int) value;
			} else {
				LOG.warn("Configuration value {} overflows/underflows the integer type.", value);
				return defaultValue;
			}
		}
		else {
			try {
				return Integer.parseInt(o.toString());
			}
			catch (NumberFormatException e) {
				LOG.warn("Configuration cannot evaluate value {} as an integer number", o);
				return defaultValue;
			}
		}
	}