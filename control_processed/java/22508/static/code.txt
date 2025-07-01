private void switchChannelStatus(final Long channelId, final ChannelStatus channelStatus) {
        transactionTemplate.execute(new TransactionCallbackWithoutResult() {

            @Override
            protected void doInTransactionWithoutResult(TransactionStatus status) {
                try {
                    final ChannelDO channelDo = channelDao.findById(channelId);

                    if (null == channelDo) {
                        String exceptionCause = "query channelId:" + channelId + " return null.";
                        logger.error("ERROR ## " + exceptionCause);
                        throw new ManagerException(exceptionCause);
                    }

                    ChannelStatus oldStatus = arbitrateManageService.channelEvent().status(channelDo.getId());
                    Channel channel = doToModel(channelDo);
                    // 检查下ddl/home配置
                    List<Pipeline> pipelines = channel.getPipelines();
                    if (pipelines.size() > 1) {
                        boolean ddlSync = true;
                        boolean homeSync = true;
                        for (Pipeline pipeline : pipelines) {
                            homeSync &= pipeline.getParameters().isHome();
                            ddlSync &= pipeline.getParameters().getDdlSync();
                        }

                        if (ddlSync) {
                            throw new InvalidConfigureException(INVALID_TYPE.DDL);
                        }

                        if (homeSync) {
                            throw new InvalidConfigureException(INVALID_TYPE.HOME);
                        }
                    }

                    channel.setStatus(oldStatus);
                    ChannelStatus newStatus = channelStatus;
                    if (newStatus != null) {
                        if (newStatus.equals(oldStatus)) {
                            // String exceptionCause = "switch the channel(" +
                            // channelId + ") status to " +
                            // channelStatus
                            // + " but it had the status:" + oldStatus;
                            // logger.error("ERROR ## " + exceptionCause);
                            // throw new ManagerException(exceptionCause);
                            // ignored
                            return;
                        } else {
                            channel.setStatus(newStatus);// 强制修改为当前变更状态
                        }
                    } else {
                        newStatus = oldStatus;
                    }

                    // 针对关闭操作，要优先更改对应的status，避免node工作线程继续往下跑
                    if (newStatus.isStop()) {
                        arbitrateManageService.channelEvent().stop(channelId);
                    } else if (newStatus.isPause()) {
                        arbitrateManageService.channelEvent().pause(channelId);
                    }

                    // 通知变更内容
                    boolean result = configRemoteService.notifyChannel(channel);// 客户端响应成功，才更改对应的状态

                    if (result) {
                        // 针对启动的话，需要先通知到客户端，客户端启动线程后，再更改channel状态
                        if (newStatus.isStart()) {
                            arbitrateManageService.channelEvent().start(channelId);
                        }
                    }

                } catch (Exception e) {
                    logger.error("ERROR ## switch the channel(" + channelId + ") status has an exception.");
                    throw new ManagerException(e);
                }
            }
        });

    }