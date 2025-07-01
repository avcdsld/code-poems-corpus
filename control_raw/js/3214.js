function(bounds, p1, p2)
	{
		var top = bounds.y;
		var left = bounds.x;
		var bottom = top + bounds.height;
		var right = left + bounds.width;
			
		// Find min and max X for the segment
		var minX = p1.x;
		var maxX = p2.x;
		
		if (p1.x > p2.x)
		{
		  minX = p2.x;
		  maxX = p1.x;
		}
		
		// Find the intersection of the segment's and rectangle's x-projections
		if (maxX > right)
		{
		  maxX = right;
		}
		
		if (minX < left)
		{
		  minX = left;
		}
		
		if (minX > maxX) // If their projections do not intersect return false
		{
		  return false;
		}
		
		// Find corresponding min and max Y for min and max X we found before
		var minY = p1.y;
		var maxY = p2.y;
		var dx = p2.x - p1.x;
		
		if (Math.abs(dx) > 0.0000001)
		{
		  var a = (p2.y - p1.y) / dx;
		  var b = p1.y - a * p1.x;
		  minY = a * minX + b;
		  maxY = a * maxX + b;
		}
		
		if (minY > maxY)
		{
		  var tmp = maxY;
		  maxY = minY;
		  minY = tmp;
		}
		
		// Find the intersection of the segment's and rectangle's y-projections
		if (maxY > bottom)
		{
		  maxY = bottom;
		}
		
		if (minY < top)
		{
		  minY = top;
		}
		
		if (minY > maxY) // If Y-projections do not intersect return false
		{
		  return false;
		}
		
		return true;
	}