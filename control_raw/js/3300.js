function mxGraphHierarchyNode(cell)
{
	mxGraphAbstractHierarchyCell.apply(this, arguments);
	this.cell = cell;
	this.id = mxObjectIdentity.get(cell);
	this.connectsAsTarget = [];
	this.connectsAsSource = [];
}