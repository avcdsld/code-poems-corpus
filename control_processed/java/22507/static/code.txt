public List<Channel> listByNodeId(Long nodeId, ChannelStatus... statuses) {
        List<Channel> channels = new ArrayList<Channel>();
        List<Channel> results = new ArrayList<Channel>();
        try {
            List<Pipeline> pipelines = pipelineService.listByNodeId(nodeId);
            List<Long> pipelineIds = new ArrayList<Long>();
            for (Pipeline pipeline : pipelines) {
                pipelineIds.add(pipeline.getId());
            }

            if (pipelineIds.isEmpty()) { // 没有关联任务直接返回
                return channels;
            }

            // 反查对应的channel
            channels = listByPipelineIds(pipelineIds.toArray(new Long[pipelineIds.size()]));
            if (null == statuses || statuses.length == 0) {
                return channels;
            }

            for (Channel channel : channels) {
                for (ChannelStatus status : statuses) {
                    if (channel.getStatus().equals(status)) {
                        results.add(channel);
                    }
                }
            }
        } catch (Exception e) {
            logger.error("ERROR ## list query channel by nodeId:" + nodeId + " has an exception!");
            throw new ManagerException(e);
        }
        return results;
    }