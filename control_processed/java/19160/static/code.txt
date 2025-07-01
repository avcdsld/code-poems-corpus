public void createCluster() {
        AmazonElasticMapReduce emr = sparkEmrClientBuilder.build();
        Optional<ClusterSummary> csr = findClusterWithName(emr, sparkClusterName);
        if (csr.isPresent()) {
            String msg = String.format("A cluster with name %s and id %s is already deployed", sparkClusterName, csr.get().getId());
            log.error(msg);
            throw new IllegalStateException(msg);
        } else {
            RunJobFlowResult res = emr.runJobFlow(sparkRunJobFlowRequest);
            String msg = String.format("Your cluster is launched with name %s and id %s.", sparkClusterName, res.getJobFlowId());
            log.info(msg);
        }

    }