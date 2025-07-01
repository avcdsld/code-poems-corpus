@Inject
    public void setReporterConfiguration(@Nullable JaegerReporterConfiguration reporterConfiguration) {
        if (reporterConfiguration != null) {
            configuration.withReporter(reporterConfiguration.configuration);
        }
    }