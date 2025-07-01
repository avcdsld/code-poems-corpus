function(node, before)
	{
		var tmp = (before) ? node.previousSibling : node.nextSibling;
		
		while (tmp != null && tmp.nodeType == mxConstants.NODETYPE_TEXT)
		{
			var next = (before) ? tmp.previousSibling : tmp.nextSibling;
			var text = mxUtils.getTextContent(tmp);
			
			if (mxUtils.trim(text).length == 0)
			{
				tmp.parentNode.removeChild(tmp);
			}
			
			tmp = next;
		}
	}