private static List<String> filterSupportedPropertiesFactorySpecific(
		TableFactory factory,
		List<String> keys) {

		if (factory instanceof TableFormatFactory) {
			boolean includeSchema = ((TableFormatFactory) factory).supportsSchemaDerivation();
			return keys.stream().filter(k -> {
				if (includeSchema) {
					return k.startsWith(Schema.SCHEMA + ".") ||
						k.startsWith(FormatDescriptorValidator.FORMAT + ".");
				} else {
					return k.startsWith(FormatDescriptorValidator.FORMAT + ".");
				}
			}).collect(Collectors.toList());
		} else {
			return keys;
		}
	}