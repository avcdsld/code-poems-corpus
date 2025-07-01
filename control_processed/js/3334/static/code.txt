function pushPoint(pt)
		{
			if (lastPushed == null || Math.abs(lastPushed.x - pt.x) >= tol || Math.abs(lastPushed.y - pt.y) >= tol)
			{
				result.push(pt);
				lastPushed = pt;
			}
			
			return lastPushed;
		}