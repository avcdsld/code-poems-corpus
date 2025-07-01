function(oMetadata, oXMLDoc, sSourceUrl) {
		try {
			AnnotationParser._parserData = {};
			AnnotationParser._oXPath = AnnotationParser.getXPath();

			return AnnotationParser._parse(oMetadata, oXMLDoc, sSourceUrl);
		} finally {
			delete AnnotationParser._parserData;
			delete AnnotationParser._oXPath;
		}
	}