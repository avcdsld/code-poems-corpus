function mxEdgeHandler(state)
{
	if (state != null)
	{
		this.state = state;
		this.init();
		
		// Handles escape keystrokes
		this.escapeHandler = mxUtils.bind(this, function(sender, evt)
		{
			var dirty = this.index != null;
			this.reset();
			
			if (dirty)
			{
				this.graph.cellRenderer.redraw(this.state, false, state.view.isRendering());
			}
		});
		
		this.state.view.graph.addListener(mxEvent.ESCAPE, this.escapeHandler);
	}
}