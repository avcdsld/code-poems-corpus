public Builder clear() {
      traceId = null;
      parentId = null;
      id = null;
      kind = null;
      name = null;
      timestamp = 0L;
      duration = 0L;
      localEndpoint = null;
      remoteEndpoint = null;
      if (annotations != null) annotations.clear();
      if (tags != null) tags.clear();
      flags = 0;
      return this;
    }