private DelayStat delayStatDOToModel(DelayStatDO delayStatDO) {
        DelayStat delayStat = new DelayStat();
        delayStat.setId(delayStatDO.getId());
        delayStat.setDelayTime(delayStatDO.getDelayTime());
        delayStat.setDelayNumber(delayStatDO.getDelayNumber());
        delayStat.setPipelineId(delayStatDO.getPipelineId());
        delayStat.setGmtCreate(delayStatDO.getGmtCreate());
        delayStat.setGmtModified(delayStatDO.getGmtModified());
        return delayStat;

    }