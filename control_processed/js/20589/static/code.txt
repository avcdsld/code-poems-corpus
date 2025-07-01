function()
  {
    // get the array of chunks whose contents need to be fetched
    var buffer = chunks.slice(start, start + prefetchSize + 1);

    // the first chunk in the buffer is the next chunk we want to load
    var nextChunk = buffer[0];

    // if we don't have anymore chunks to load, we're done
    if (!nextChunk)
    {
      self.asyncClose();
    }
    else
    {
      // fire off requests to load all the chunks in the buffer that aren't
      // already loading
      var chunk, index, length;
      for (index = 0, length = buffer.length; index < length; index++)
      {
        chunk = buffer[index];
        if (!chunk.isLoading())
        {
          chunk.load();
        }
      }

      // subscribe to the loadcomplete event on the next chunk
      nextChunk.on('loadcomplete', onLoadComplete);
    }
  }