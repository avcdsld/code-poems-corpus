function(lan)
	{
		if (mxClient.languages != null)
		{
			return mxUtils.indexOf(mxClient.languages, lan) >= 0;
		}
		
		return true;
	}