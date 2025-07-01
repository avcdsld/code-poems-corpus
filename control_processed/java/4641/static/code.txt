@Override
	public void configure(Configuration parameters) {

		// enforce sequential configure() calls
		synchronized (CONFIGURE_MUTEX) {
			if (this.mapreduceOutputFormat instanceof Configurable) {
				((Configurable) this.mapreduceOutputFormat).setConf(this.configuration);
			}
		}
	}