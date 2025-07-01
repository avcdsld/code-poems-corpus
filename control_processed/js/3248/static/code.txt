function(element, graphF, funct, dragElement, dx, dy, autoscroll,
			scalePreview, highlightDropTargets, getDropTarget)
	{
		var dragSource = new mxDragSource(element, funct);
		dragSource.dragOffset = new mxPoint((dx != null) ? dx : 0,
			(dy != null) ? dy : mxConstants.TOOLTIP_VERTICAL_OFFSET);
		dragSource.autoscroll = autoscroll;
		
		// Cannot enable this by default. This needs to be enabled in the caller
		// if the funct argument uses the new x- and y-arguments.
		dragSource.setGuidesEnabled(false);
		
		if (highlightDropTargets != null)
		{
			dragSource.highlightDropTargets = highlightDropTargets;
		}
		
		// Overrides function to find drop target cell
		if (getDropTarget != null)
		{
			dragSource.getDropTarget = getDropTarget;
		}
		
		// Overrides function to get current graph
		dragSource.getGraphForEvent = function(evt)
		{
			return (typeof(graphF) == 'function') ? graphF(evt) : graphF;
		};
		
		// Translates switches into dragSource customizations
		if (dragElement != null)
		{
			dragSource.createDragElement = function()
			{
				return dragElement.cloneNode(true);
			};
			
			if (scalePreview)
			{
				dragSource.createPreviewElement = function(graph)
				{
					var elt = dragElement.cloneNode(true);

					var w = parseInt(elt.style.width);
					var h = parseInt(elt.style.height);
					elt.style.width = Math.round(w * graph.view.scale) + 'px';
					elt.style.height = Math.round(h * graph.view.scale) + 'px';
					
					return elt;
				};
			}
		}
		
		return dragSource;
	}