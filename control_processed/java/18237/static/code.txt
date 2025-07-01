public static KerasTokenizer fromJson(String jsonFileName) throws IOException, InvalidKerasConfigurationException {
        String json = new String(Files.readAllBytes(Paths.get(jsonFileName)));
        Map<String, Object> tokenizerBaseConfig = parseJsonString(json);
        Map<String, Object> tokenizerConfig;
        if (tokenizerBaseConfig.containsKey("config"))
            tokenizerConfig = (Map<String, Object>) tokenizerBaseConfig.get("config");
        else
            throw new InvalidKerasConfigurationException("No configuration found for Keras tokenizer");


        Integer numWords = (Integer) tokenizerConfig.get("num_words");
        String filters = (String) tokenizerConfig.get("filters");
        Boolean lower = (Boolean) tokenizerConfig.get("lower");
        String split = (String) tokenizerConfig.get("split");
        Boolean charLevel = (Boolean) tokenizerConfig.get("char_level");
        String oovToken = (String) tokenizerConfig.get("oov_token");
        Integer documentCount = (Integer) tokenizerConfig.get("document_count");

        @SuppressWarnings("unchecked")
        Map<String, Integer> wordCounts = (Map) parseJsonString((String) tokenizerConfig.get("word_counts"));
        @SuppressWarnings("unchecked")
        Map<String, Integer> wordDocs = (Map) parseJsonString((String) tokenizerConfig.get("word_docs"));
        @SuppressWarnings("unchecked")
        Map<String, Integer> wordIndex = (Map) parseJsonString((String) tokenizerConfig.get("word_index"));
        @SuppressWarnings("unchecked")
        Map<Integer, String> indexWord = (Map) parseJsonString((String) tokenizerConfig.get("index_word"));
        @SuppressWarnings("unchecked")
        Map<Integer, Integer> indexDocs = (Map) parseJsonString((String) tokenizerConfig.get("index_docs"));

        KerasTokenizer tokenizer = new KerasTokenizer(numWords, filters, lower, split, charLevel, oovToken);
        tokenizer.setDocumentCount(documentCount);
        tokenizer.setWordCounts(wordCounts);
        tokenizer.setWordDocs(new HashMap<>(wordDocs));
        tokenizer.setWordIndex(wordIndex);
        tokenizer.setIndexWord(indexWord);
        tokenizer.setIndexDocs(indexDocs);

        return tokenizer;
    }