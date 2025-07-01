protected void emitRecord(
			T record,
			KafkaTopicPartitionState<TopicPartition> partition,
			long offset,
			@SuppressWarnings("UnusedParameters") ConsumerRecord<?, ?> consumerRecord) throws Exception {

		// the 0.9 Fetcher does not try to extract a timestamp
		emitRecord(record, partition, offset);
	}