def defaults
      { tags:        nil,
        writer:      :socket,
        noop:        false,
        novalidate:  false,
        noauto:      false,
        verbose:     false,
        debug:       false,
        chunk_size:  1000,
        chunk_pause: 0 }
    end