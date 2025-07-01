@POST
  @Path("/worker")
  @Consumes(MediaType.APPLICATION_JSON)
  @ResourceFilters(ConfigResourceFilter.class)
  public Response setWorkerConfig(
      final WorkerBehaviorConfig workerBehaviorConfig,
      @HeaderParam(AuditManager.X_DRUID_AUTHOR) @DefaultValue("") final String author,
      @HeaderParam(AuditManager.X_DRUID_COMMENT) @DefaultValue("") final String comment,
      @Context final HttpServletRequest req
  )
  {
    final SetResult setResult = configManager.set(
        WorkerBehaviorConfig.CONFIG_KEY,
        workerBehaviorConfig,
        new AuditInfo(author, comment, req.getRemoteAddr())
    );
    if (setResult.isOk()) {
      log.info("Updating Worker configs: %s", workerBehaviorConfig);

      return Response.ok().build();
    } else {
      return Response.status(Response.Status.BAD_REQUEST).build();
    }
  }