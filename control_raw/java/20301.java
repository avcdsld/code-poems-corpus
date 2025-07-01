public static String buildCleanedParametersURIRepresentation(org.apache.commons.httpclient.URI uri,
			SpiderParam.HandleParametersOption handleParameters, boolean handleODataParametersVisited) throws URIException {
		// If the option is set to use all the information, just use the default string representation
		if (handleParameters.equals(HandleParametersOption.USE_ALL)) {
			return uri.toString();
		}

		// If the option is set to ignore parameters completely, ignore the query completely
		if (handleParameters.equals(HandleParametersOption.IGNORE_COMPLETELY)) {
			return createBaseUriWithCleanedPath(uri, handleParameters, handleODataParametersVisited);
		}

		// If the option is set to ignore the value, we get the parameters and we only add their name to the
		// query
		if (handleParameters.equals(HandleParametersOption.IGNORE_VALUE)) {
			StringBuilder retVal = new StringBuilder(
					createBaseUriWithCleanedPath(uri, handleParameters, handleODataParametersVisited));
			
			String cleanedQuery = getCleanedQuery(uri.getEscapedQuery());
			
			// Add the parameters' names to the uri representation. 
			if(cleanedQuery.length()>0) {
				retVal.append('?').append(cleanedQuery);
			}

			return retVal.toString();
		}

		// Should not be reached
		return uri.toString();
	}