function(a, b)
	{
		var tw = a.width;
		var th = a.height;
		var rw = b.width;
		var rh = b.height;
		
		if (rw <= 0 || rh <= 0 || tw <= 0 || th <= 0)
		{
		    return false;
		}
		
		var tx = a.x;
		var ty = a.y;
		var rx = b.x;
		var ry = b.y;
		
		rw += rx;
		rh += ry;
		tw += tx;
		th += ty;

		return ((rw < rx || rw > tx) &&
			(rh < ry || rh > ty) &&
			(tw < tx || tw > rx) &&
			(th < ty || th > ry));
	}