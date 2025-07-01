function mxTooltipHandler(graph, delay)
{
	if (graph != null)
	{
		this.graph = graph;
		this.delay = delay || 500;
		this.graph.addMouseListener(this);
	}
}