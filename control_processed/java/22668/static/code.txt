public List<DataMediaPair> listByPipelineId(Long pipelineId) {
        Assert.assertNotNull(pipelineId);
        List<DataMediaPair> dataMediaPairs = new ArrayList<DataMediaPair>();
        try {
            List<DataMediaPairDO> dataMediaPairDos = dataMediaPairDao.listByPipelineId(pipelineId);
            if (dataMediaPairDos.isEmpty()) {
                logger.debug("DEBUG ## couldn't query any dataMediaPair, maybe hasn't create any dataMediaPair.");
                return dataMediaPairs;
            }
            dataMediaPairs = doToModel(dataMediaPairDos);
        } catch (Exception e) {
            logger.error("ERROR ## query dataMediaPairs by pipelineId:" + pipelineId + " has an exception!", e);
            throw new ManagerException(e);
        }

        return dataMediaPairs;
    }