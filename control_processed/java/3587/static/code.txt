public FlinkKafkaConsumerBase<T> assignTimestampsAndWatermarks(AssignerWithPunctuatedWatermarks<T> assigner) {
		checkNotNull(assigner);

		if (this.periodicWatermarkAssigner != null) {
			throw new IllegalStateException("A periodic watermark emitter has already been set.");
		}
		try {
			ClosureCleaner.clean(assigner, true);
			this.punctuatedWatermarkAssigner = new SerializedValue<>(assigner);
			return this;
		} catch (Exception e) {
			throw new IllegalArgumentException("The given assigner is not serializable", e);
		}
	}