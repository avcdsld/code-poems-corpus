public WaterMeterCpuTicks createImpl() {
    WaterMeterCpuTicks obj = new WaterMeterCpuTicks();
    PojoUtils.copyProperties(obj, this, PojoUtils.FieldNaming.CONSISTENT);
    return obj;
  }