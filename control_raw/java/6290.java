private void setProperty(ColumnFamilyHandle handle, String property, RocksDBNativeMetricView metricView) {
		if (metricView.isClosed()) {
			return;
		}
		try {
			synchronized (lock) {
				if (rocksDB != null) {
					long value = rocksDB.getLongProperty(handle, property);
					metricView.setValue(value);
				}
			}
		} catch (RocksDBException e) {
			metricView.close();
			LOG.warn("Failed to read native metric %s from RocksDB", property, e);
		}
	}