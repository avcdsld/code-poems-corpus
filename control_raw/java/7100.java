protected Map<String, String> getReversedMapping() {
		 return (null != this.fieldMapping) ? MapUtil.reverse(this.fieldMapping) : null;
	}