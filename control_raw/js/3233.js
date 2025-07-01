function(style)
	{
		var result = [];
		
		if (style != null)
		{
			var pairs = style.split(';');
			
			for (var i = 0; i < pairs.length; i++)
			{
				if (pairs[i].indexOf('=') < 0)
				{
					result.push(pairs[i]);
				}
			}
		}
				
		return result;
	}