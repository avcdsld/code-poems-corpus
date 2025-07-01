public TaskSchedulerBuilder customizers(
			Iterable<TaskSchedulerCustomizer> customizers) {
		Assert.notNull(customizers, "Customizers must not be null");
		return new TaskSchedulerBuilder(this.poolSize, this.awaitTermination,
				this.awaitTerminationPeriod, this.threadNamePrefix,
				append(null, customizers));
	}