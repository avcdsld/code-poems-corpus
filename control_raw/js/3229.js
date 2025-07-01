function(node, value)
	{
		if (mxUtils.isVml(node))
		{
	    	if (value >= 100)
	    	{
	    		node.style.filter = '';
	    	}
	    	else
	    	{
	    		// TODO: Why is the division by 5 needed in VML?
			    node.style.filter = 'alpha(opacity=' + (value/5) + ')';
	    	}
		}
		else if (mxClient.IS_IE && (typeof(document.documentMode) === 'undefined' || document.documentMode < 9))
	    {
	    	if (value >= 100)
	    	{
	    		node.style.filter = '';
	    	}
	    	else
	    	{
			    node.style.filter = 'alpha(opacity=' + value + ')';
	    	}
		}
		else
		{
		    node.style.opacity = (value / 100);
		}
	}