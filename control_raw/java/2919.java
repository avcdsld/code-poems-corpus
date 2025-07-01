@Deprecated
	public void init(
			Map<EventId, Lockable<V>> events,
			Map<NodeId, Lockable<SharedBufferNode>> entries) throws Exception {
		eventsBuffer.putAll(events);
		this.entries.putAll(entries);

		Map<Long, Integer> maxIds = events.keySet().stream().collect(Collectors.toMap(
			EventId::getTimestamp,
			EventId::getId,
			Math::max
		));
		eventsCount.putAll(maxIds);
	}