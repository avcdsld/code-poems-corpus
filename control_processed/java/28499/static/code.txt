public final ScanRun startScanRun(String name) {

    StartScanRunRequest request = StartScanRunRequest.newBuilder().setName(name).build();
    return startScanRun(request);
  }