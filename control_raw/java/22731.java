public void remove(final Long pipelineId) {
        Assert.assertNotNull(pipelineId);
        transactionTemplate.execute(new TransactionCallbackWithoutResult() {

            @Override
            protected void doInTransactionWithoutResult(TransactionStatus status) {
                try {
                    PipelineDO pipelineDO = pipelineDao.findById(pipelineId);
                    if (pipelineDO != null) {
                        pipelineDao.delete(pipelineId);
                        pipelineNodeRelationDao.deleteByPipelineId(pipelineId);
                        // 删除历史cursor
                        String destination = pipelineDO.getParameters().getDestinationName();
                        short clientId = pipelineDO.getId().shortValue();
                        arbitrateViewService.removeCanal(destination, clientId);
                        arbitrateManageService.pipelineEvent().destory(pipelineDO.getChannelId(), pipelineId);
                    }
                } catch (Exception e) {
                    logger.error("ERROR ## remove the pipeline(" + pipelineId + ") has an exception!");
                    throw new ManagerException(e);
                }
            }
        });
    }