public static void run(StreamFunctionExecutor functionExecutor, String... args) {
        parseData(args, (data, isDebug) -> {
            try (InputStream input = data != null ? new ByteArrayInputStream(data.getBytes(StandardCharsets.UTF_8)) : System.in) {
                functionExecutor.execute(input, System.out);
            } catch (Exception e) {
                exitWithError(isDebug, e);
            }
        });
    }