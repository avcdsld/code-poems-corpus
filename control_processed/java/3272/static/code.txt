private static void writeJobDetails(ExecutionEnvironment env, String jobDetailsPath) throws IOException {
		JobExecutionResult result = env.getLastJobExecutionResult();

		File jsonFile = new File(jobDetailsPath);

		try (JsonGenerator json = new JsonFactory().createGenerator(jsonFile, JsonEncoding.UTF8)) {
			json.writeStartObject();

			json.writeObjectFieldStart("Apache Flink");
			json.writeStringField("version", EnvironmentInformation.getVersion());
			json.writeStringField("commit ID", EnvironmentInformation.getRevisionInformation().commitId);
			json.writeStringField("commit date", EnvironmentInformation.getRevisionInformation().commitDate);
			json.writeEndObject();

			json.writeStringField("job_id", result.getJobID().toString());
			json.writeNumberField("runtime_ms", result.getNetRuntime());

			json.writeObjectFieldStart("parameters");
			for (Map.Entry<String, String> entry : env.getConfig().getGlobalJobParameters().toMap().entrySet()) {
				json.writeStringField(entry.getKey(), entry.getValue());
			}
			json.writeEndObject();

			json.writeObjectFieldStart("accumulators");
			for (Map.Entry<String, Object> entry : result.getAllAccumulatorResults().entrySet()) {
				json.writeStringField(entry.getKey(), entry.getValue().toString());
			}
			json.writeEndObject();

			json.writeEndObject();
		}
	}