public void setFields(List<Field> fields) throws SqlParseException {
		/*
		zhongshu-comment select * from tbl_a;
		select * 这种sql语句的select.getFields().size()为0
		 */
		if (select.getFields().size() > 0) {
			ArrayList<String> includeFields = new ArrayList<String>();
			ArrayList<String> excludeFields = new ArrayList<String>();

			for (Field field : fields) {
				if (field instanceof MethodField) { //zhongshu-comment MethodField是Field的子类，而且Field也就只有MethodField这一个子类了
					MethodField method = (MethodField) field;
					if (method.getName().toLowerCase().equals("script")) {
						/*
						zhongshu-comment scripted_field only allows script(name,script) or script(name,lang,script)
						script类型的MethodField是不会加到include和exclude中的
						 */
						handleScriptField(method);
					} else if (method.getName().equalsIgnoreCase("include")) {
					    String f;
						for (KVValue kvValue : method.getParams()) {
							//zhongshu-comment select a,b,c 中的a、b、c字段add到includeFields中
                            f = kvValue.value.toString();
                            fieldNames.add(f);
                            includeFields.add(f);
						}
					} else if (method.getName().equalsIgnoreCase("exclude")) {
						for (KVValue kvValue : method.getParams()) {
							excludeFields.add(kvValue.value.toString()) ;
						}
					}
				} else if (field != null) {
                    fieldNames.add(field.getName());
					includeFields.add(field.getName());
				}
			}

			request.setFetchSource(
					includeFields.toArray(new String[includeFields.size()]),
					excludeFields.toArray(new String[excludeFields.size()])
			);
		}
	}