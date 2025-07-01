private Pipeline doToModel(PipelineDO pipelineDo) {
        Pipeline pipeline = new Pipeline();
        try {
            pipeline.setId(pipelineDo.getId());
            pipeline.setName(pipelineDo.getName());
            pipeline.setParameters(pipelineDo.getParameters());
            pipeline.setDescription(pipelineDo.getDescription());
            pipeline.setGmtCreate(pipelineDo.getGmtCreate());
            pipeline.setGmtModified(pipelineDo.getGmtModified());
            pipeline.setChannelId(pipelineDo.getChannelId());
            pipeline.getParameters().setMainstemClientId(pipeline.getId().shortValue());

            // 组装DatamediaPair
            List<DataMediaPair> pairs = dataMediaPairService.listByPipelineId(pipelineDo.getId());
            Collections.sort(pairs, new DataMediaPairComparable());
            pipeline.setPairs(pairs);

            // 组装Node
            List<PipelineNodeRelationDO> relations = pipelineNodeRelationDao.listByPipelineIds(pipelineDo.getId());

            List<Long> totalNodeIds = new ArrayList<Long>();

            for (PipelineNodeRelationDO relation : relations) {
                Long nodeId = relation.getNodeId();
                if (!totalNodeIds.contains(nodeId)) {
                    totalNodeIds.add(nodeId);
                }
            }

            List<Node> totalNodes = nodeService.listByIds(totalNodeIds.toArray(new Long[totalNodeIds.size()]));
            List<Node> selectNodes = new ArrayList<Node>();
            List<Node> extractNodes = new ArrayList<Node>();
            List<Node> loadNodes = new ArrayList<Node>();

            for (Node node : totalNodes) {
                for (PipelineNodeRelationDO relation : relations) {
                    if (node.getId().equals(relation.getNodeId())) {
                        if (relation.getLocation().isSelect()) {
                            selectNodes.add(node);
                        } else if (relation.getLocation().isExtract()) {
                            extractNodes.add(node);
                        } else if (relation.getLocation().isLoad()) {
                            loadNodes.add(node);
                        }
                    }
                }
            }

            pipeline.setSelectNodes(selectNodes);
            pipeline.setExtractNodes(extractNodes);
            pipeline.setLoadNodes(loadNodes);

        } catch (Exception e) {
            logger.error("ERROR ## change the pipeline Do to Model has an exception");
            throw new ManagerException(e);
        }

        return pipeline;
    }