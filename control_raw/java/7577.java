public static CombinationAnnotationElement toCombination(AnnotatedElement annotationEle) {
		if(annotationEle instanceof CombinationAnnotationElement) {
			return (CombinationAnnotationElement)annotationEle;
		}
		return new CombinationAnnotationElement(annotationEle);
	}