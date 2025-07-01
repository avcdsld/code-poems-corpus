public static Collection<ArchivedJson> getArchivedJsons(Path file) throws IOException {
		try (FSDataInputStream input = file.getFileSystem().open(file);
			ByteArrayOutputStream output = new ByteArrayOutputStream()) {
			IOUtils.copyBytes(input, output);

			JsonNode archive = mapper.readTree(output.toByteArray());

			Collection<ArchivedJson> archives = new ArrayList<>();
			for (JsonNode archivePart : archive.get(ARCHIVE)) {
				String path = archivePart.get(PATH).asText();
				String json = archivePart.get(JSON).asText();
				archives.add(new ArchivedJson(path, json));
			}
			return archives;
		}
	}