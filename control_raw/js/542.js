function Edge(n1, n2, dataIndex) {

    /**
     * 节点1，如果是有向图则为源节点
     * @type {module:echarts/data/Graph.Node}
     */
    this.node1 = n1;

    /**
     * 节点2，如果是有向图则为目标节点
     * @type {module:echarts/data/Graph.Node}
     */
    this.node2 = n2;

    this.dataIndex = dataIndex == null ? -1 : dataIndex;
}