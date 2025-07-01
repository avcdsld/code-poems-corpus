public Cluster setCluster(Cluster newCluster) {
        // 开始切换
        Cluster old = this.cluster;
        this.cluster = newCluster;
        return old;
    }