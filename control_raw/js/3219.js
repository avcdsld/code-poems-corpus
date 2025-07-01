function(doc)
	{
		if (mxClient.IS_QUIRKS)
		{
			return new mxPoint(doc.body.scrollLeft, doc.body.scrollTop);
		}
		else
		{
			var wnd = doc.defaultView || doc.parentWindow;
			
			var x = (wnd != null && window.pageXOffset !== undefined) ? window.pageXOffset : (document.documentElement || document.body.parentNode || document.body).scrollLeft;
			var y = (wnd != null && window.pageYOffset !== undefined) ? window.pageYOffset : (document.documentElement || document.body.parentNode || document.body).scrollTop;
			
			return new mxPoint(x, y);
		}
	}