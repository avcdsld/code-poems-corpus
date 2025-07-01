static SelectTraceIdsFromSpan.Factory initialiseSelectTraceIdsFromSpan(Session session) {
    try {
      return new SelectTraceIdsFromSpan.Factory(session);
    } catch (DriverException ex) {
      LOG.warn("failed to prepare annotation_query index statements: " + ex.getMessage());
      return null;
    }
  }