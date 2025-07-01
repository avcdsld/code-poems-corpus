public Builder merge(Span source) {
      if (traceId == null) traceId = source.traceId;
      if (id == null) id = source.id;
      if (parentId == null) parentId = source.parentId;
      if (kind == null) kind = source.kind;
      if (name == null) name = source.name;
      if (timestamp == 0L) timestamp = source.timestamp;
      if (duration == 0L) duration = source.duration;
      if (localEndpoint == null) {
        localEndpoint = source.localEndpoint;
      } else if (source.localEndpoint != null) {
        localEndpoint = localEndpoint.toBuilder().merge(source.localEndpoint).build();
      }
      if (remoteEndpoint == null) {
        remoteEndpoint = source.remoteEndpoint;
      } else if (source.remoteEndpoint != null) {
        remoteEndpoint = remoteEndpoint.toBuilder().merge(source.remoteEndpoint).build();
      }
      if (!source.annotations.isEmpty()) {
        if (annotations == null) {
          annotations = new ArrayList<>(source.annotations.size());
        }
        annotations.addAll(source.annotations);
      }
      if (!source.tags.isEmpty()) {
        if (tags == null) tags = new TreeMap<>();
        tags.putAll(source.tags);
      }
      flags = flags | source.flags;
      return this;
    }