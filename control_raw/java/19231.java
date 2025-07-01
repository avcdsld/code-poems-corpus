public KerasModelBuilder modelYamlFilename(String modelYamlFilename) throws IOException {
        checkForExistence(modelYamlFilename);
        this.modelJson = new String(Files.readAllBytes(Paths.get(modelYamlFilename)));
        return this;
    }