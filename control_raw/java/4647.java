public List<FieldReferenceExpression> getAllInputFields() {
		return fieldReferences.stream().flatMap(input -> input.values().stream()).collect(toList());
	}