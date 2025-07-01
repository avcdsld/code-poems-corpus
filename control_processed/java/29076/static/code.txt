@BetaApi
  public final Operation resizeRegionDisk(
      ProjectRegionDiskName disk, RegionDisksResizeRequest regionDisksResizeRequestResource) {

    ResizeRegionDiskHttpRequest request =
        ResizeRegionDiskHttpRequest.newBuilder()
            .setDisk(disk == null ? null : disk.toString())
            .setRegionDisksResizeRequestResource(regionDisksResizeRequestResource)
            .build();
    return resizeRegionDisk(request);
  }