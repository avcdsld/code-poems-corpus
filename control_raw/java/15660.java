public boolean loadSegment(final DataSegment segment) throws SegmentLoadingException
  {
    final Segment adapter = getAdapter(segment);

    final SettableSupplier<Boolean> resultSupplier = new SettableSupplier<>();

    // compute() is used to ensure that the operation for a data source is executed atomically
    dataSources.compute(
        segment.getDataSource(),
        (k, v) -> {
          final DataSourceState dataSourceState = v == null ? new DataSourceState() : v;
          final VersionedIntervalTimeline<String, ReferenceCountingSegment> loadedIntervals =
              dataSourceState.getTimeline();
          final PartitionHolder<ReferenceCountingSegment> entry = loadedIntervals.findEntry(
              segment.getInterval(),
              segment.getVersion()
          );

          if ((entry != null) && (entry.getChunk(segment.getShardSpec().getPartitionNum()) != null)) {
            log.warn("Told to load an adapter for segment[%s] that already exists", segment.getId());
            resultSupplier.set(false);
          } else {
            loadedIntervals.add(
                segment.getInterval(),
                segment.getVersion(),
                segment.getShardSpec().createChunk(new ReferenceCountingSegment(adapter))
            );
            dataSourceState.addSegment(segment);
            resultSupplier.set(true);
          }
          return dataSourceState;
        }
    );

    return resultSupplier.get();
  }