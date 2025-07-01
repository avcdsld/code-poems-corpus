public static ValidationResult isValidAddOn(Path file) {
		if (file == null || file.getNameCount() == 0) {
			return new ValidationResult(ValidationResult.Validity.INVALID_PATH);
		}

		if (!isAddOnFileName(file.getFileName().toString())) {
			return new ValidationResult(ValidationResult.Validity.INVALID_FILE_NAME);
		}

		if (!Files.isRegularFile(file) || !Files.isReadable(file)) {
			return new ValidationResult(ValidationResult.Validity.FILE_NOT_READABLE);
		}

		try (ZipFile zip = new ZipFile(file.toFile())) {
			ZipEntry manifest = zip.getEntry(MANIFEST_FILE_NAME);
			if (manifest == null) {
				return new ValidationResult(ValidationResult.Validity.MISSING_MANIFEST);
			}

			try (InputStream zis = zip.getInputStream(manifest)) {
				try {
					return new ValidationResult(new ZapAddOnXmlFile(zis));
				} catch (Exception e) {
					return new ValidationResult(ValidationResult.Validity.INVALID_MANIFEST, e);
				}
			}
		} catch (ZipException e) {
			return new ValidationResult(ValidationResult.Validity.UNREADABLE_ZIP_FILE, e);
		} catch (Exception e) {
			return new ValidationResult(ValidationResult.Validity.IO_ERROR_FILE, e);
		}
	}