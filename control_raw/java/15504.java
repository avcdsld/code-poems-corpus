void onSealExclusive(Batch batch, long elapsedTimeMillis)
  {
    try {
      doOnSealExclusive(batch, elapsedTimeMillis);
    }
    catch (Throwable t) {
      try {
        if (!concurrentBatch.compareAndSet(batch, batch.batchNumber)) {
          log.error("Unexpected failure to set currentBatch to the failed Batch.batchNumber");
        }
        log.error(t, "Serious error during onSealExclusive(), set currentBatch to the failed Batch.batchNumber");
      }
      catch (Throwable t2) {
        t.addSuppressed(t2);
      }
      throw t;
    }
  }