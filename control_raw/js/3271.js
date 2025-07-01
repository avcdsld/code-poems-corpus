function mxDivResizer(div, container)
{
	if (div.nodeName.toLowerCase() == 'div')
	{
		if (container == null)
		{
			container = window;
		}

		this.div = div;
		var style = mxUtils.getCurrentStyle(div);
		
		if (style != null)
		{
			this.resizeWidth = style.width == 'auto';
			this.resizeHeight = style.height == 'auto';
		}
		
		mxEvent.addListener(container, 'resize',
			mxUtils.bind(this, function(evt)
			{
				if (!this.handlingResize)
				{
					this.handlingResize = true;
					this.resize();
					this.handlingResize = false;
				}
			})
		);
		
		this.resize();
	}
}