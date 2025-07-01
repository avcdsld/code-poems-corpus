public final ScanConfig createScanConfig(ProjectName parent, ScanConfig scanConfig) {

    CreateScanConfigRequest request =
        CreateScanConfigRequest.newBuilder()
            .setParent(parent == null ? null : parent.toString())
            .setScanConfig(scanConfig)
            .build();
    return createScanConfig(request);
  }