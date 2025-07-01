public static Writer render(Template templateContent, Map<String, Object> bindingMap, Writer writer) {
		templateContent.binding(bindingMap);
		templateContent.renderTo(writer);
		return writer;
	}