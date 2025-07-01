static Glossary getGlossary(String projectId, String location, String name) {
    try (TranslationServiceClient translationServiceClient = TranslationServiceClient.create()) {

      GlossaryName glossaryName =
          GlossaryName.newBuilder()
              .setProject(projectId)
              .setLocation(location)
              .setGlossary(name)
              .build();

      // Call the API
      Glossary response = translationServiceClient.getGlossary(glossaryName.toString());
      System.out.format("Got: %s\n", response.getName());
      return response;

    } catch (Exception e) {
      throw new RuntimeException("Couldn't create client.", e);
    }
  }