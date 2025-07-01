function mxText(value, bounds, align, valign, color,
	family,	size, fontStyle, spacing, spacingTop, spacingRight,
	spacingBottom, spacingLeft, horizontal, background, border,
	wrap, clipped, overflow, labelPadding, textDirection)
{
	mxShape.call(this);
	this.value = value;
	this.bounds = bounds;
	this.color = (color != null) ? color : 'black';
	this.align = (align != null) ? align : mxConstants.ALIGN_CENTER;
	this.valign = (valign != null) ? valign : mxConstants.ALIGN_MIDDLE;
	this.family = (family != null) ? family : mxConstants.DEFAULT_FONTFAMILY;
	this.size = (size != null) ? size : mxConstants.DEFAULT_FONTSIZE;
	this.fontStyle = (fontStyle != null) ? fontStyle : mxConstants.DEFAULT_FONTSTYLE;
	this.spacing = parseInt(spacing || 2);
	this.spacingTop = this.spacing + parseInt(spacingTop || 0);
	this.spacingRight = this.spacing + parseInt(spacingRight || 0);
	this.spacingBottom = this.spacing + parseInt(spacingBottom || 0);
	this.spacingLeft = this.spacing + parseInt(spacingLeft || 0);
	this.horizontal = (horizontal != null) ? horizontal : true;
	this.background = background;
	this.border = border;
	this.wrap = (wrap != null) ? wrap : false;
	this.clipped = (clipped != null) ? clipped : false;
	this.overflow = (overflow != null) ? overflow : 'visible';
	this.labelPadding = (labelPadding != null) ? labelPadding : 0;
	this.textDirection = textDirection;
	this.rotation = 0;
	this.updateMargin();
}