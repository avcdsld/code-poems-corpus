private static String getChannelId(Long pipelineId) {
        Channel channel = ArbitrateConfigUtils.getChannel(pipelineId);
        return String.valueOf(channel.getId());
    }