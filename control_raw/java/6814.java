private void buildValuePartForIN(StringBuilder conditionStrBuilder, List<Object> paramValues) {
		conditionStrBuilder.append(" (");
		final Object value = this.value;
		if (isPlaceHolder()) {
			List<?> valuesForIn;
			// 占位符对应值列表
			if (value instanceof CharSequence) {
				valuesForIn = StrUtil.split((CharSequence) value, ',');
			} else {
				valuesForIn = Arrays.asList(Convert.convert(String[].class, value));
				if (null == valuesForIn) {
					valuesForIn = CollUtil.newArrayList(Convert.toStr(value));
				}
			}
			conditionStrBuilder.append(StrUtil.repeatAndJoin("?", valuesForIn.size(), ","));
			if(null != paramValues) {
				paramValues.addAll(valuesForIn);
			}
		} else {
			conditionStrBuilder.append(StrUtil.join(",", value));
		}
		conditionStrBuilder.append(')');
	}