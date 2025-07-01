function(x1, y1, x2, y2, px, py)
    {
		return Math.abs((y2 - y1) * px - (x2 - x1) * py + x2 * y1 - y2 * x1) /
			Math.sqrt((y2 - y1) * (y2 - y1) + (x2 - x1) * (x2 - x1));
    }