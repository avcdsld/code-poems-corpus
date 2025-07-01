public CompletableFuture<List<KeyVersion>> updateTableEntries(final String tableName,
                                                                  final List<TableEntry<byte[], byte[]>> entries,
                                                                  String delegationToken,
                                                                  final long clientRequestId) {
        final CompletableFuture<List<KeyVersion>> result = new CompletableFuture<>();
        final Controller.NodeUri uri = getTableUri(tableName);
        final WireCommandType type = WireCommandType.UPDATE_TABLE_ENTRIES;
        final long requestId = (clientRequestId == RequestTag.NON_EXISTENT_ID) ? idGenerator.get() : clientRequestId;

        final FailingReplyProcessor replyProcessor = new FailingReplyProcessor() {

            @Override
            public void connectionDropped() {
                log.warn(requestId, "updateTableEntries {} Connection dropped", tableName);
                result.completeExceptionally(new WireCommandFailedException(type, WireCommandFailedException.Reason.ConnectionDropped));
            }

            @Override
            public void wrongHost(WireCommands.WrongHost wrongHost) {
                log.warn(requestId, "updateTableEntries {} wrong host", tableName);
                result.completeExceptionally(new WireCommandFailedException(type, WireCommandFailedException.Reason.UnknownHost));
            }

            @Override
            public void noSuchSegment(WireCommands.NoSuchSegment noSuchSegment) {
                log.warn(requestId, "updateTableEntries {} NoSuchSegment", tableName);
                result.completeExceptionally(new WireCommandFailedException(type, WireCommandFailedException.Reason.SegmentDoesNotExist));
            }

            @Override
            public void tableEntriesUpdated(WireCommands.TableEntriesUpdated tableEntriesUpdated) {
                log.info(requestId, "updateTableEntries request for {} tableSegment completed.", tableName);
                result.complete(tableEntriesUpdated.getUpdatedVersions().stream().map(KeyVersionImpl::new).collect(Collectors.toList()));
            }

            @Override
            public void tableKeyDoesNotExist(WireCommands.TableKeyDoesNotExist tableKeyDoesNotExist) {
                log.warn(requestId, "updateTableEntries request for {} tableSegment failed with TableKeyDoesNotExist.", tableName);
                result.completeExceptionally(new WireCommandFailedException(type, WireCommandFailedException.Reason.TableKeyDoesNotExist));
            }

            @Override
            public void tableKeyBadVersion(WireCommands.TableKeyBadVersion tableKeyBadVersion) {
                log.warn(requestId, "updateTableEntries request for {} tableSegment failed with TableKeyBadVersion.", tableName);
                result.completeExceptionally(new WireCommandFailedException(type, WireCommandFailedException.Reason.TableKeyBadVersion));
            }

            @Override
            public void processingFailure(Exception error) {
                log.error(requestId, "updateTableEntries {} failed", tableName, error);
                handleError(error, result, type);
            }

            @Override
            public void authTokenCheckFailed(WireCommands.AuthTokenCheckFailed authTokenCheckFailed) {
                result.completeExceptionally(
                        new WireCommandFailedException(new AuthenticationException(authTokenCheckFailed.toString()),
                                                       type, WireCommandFailedException.Reason.AuthFailed));
            }
        };

        List<ByteBuf> buffersToRelease = new ArrayList<>();
        List<Map.Entry<WireCommands.TableKey, WireCommands.TableValue>> wireCommandEntries = entries.stream().map(te -> {
            final WireCommands.TableKey key = convertToWireCommand(te.getKey());
            ByteBuf valueBuffer = wrappedBuffer(te.getValue());
            buffersToRelease.add(key.getData());
            buffersToRelease.add(valueBuffer);
            final WireCommands.TableValue value = new WireCommands.TableValue(valueBuffer);
            return new AbstractMap.SimpleImmutableEntry<>(key, value);
        }).collect(Collectors.toList());

        WireCommands.UpdateTableEntries request = new WireCommands.UpdateTableEntries(requestId, tableName, delegationToken,
                                                                                      new WireCommands.TableEntries(wireCommandEntries));
        sendRequestAsync(request, replyProcessor, result, ModelHelper.encode(uri));
        return result
                .whenComplete((r, e) -> release(buffersToRelease));
    }