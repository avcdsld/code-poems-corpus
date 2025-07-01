public void generateWitherForField(JavacNode fieldNode, DiagnosticPosition pos, AccessLevel level) {
		if (hasAnnotation(Wither.class, fieldNode)) {
			//The annotation will make it happen, so we can skip it.
			return;
		}
		
		createWitherForField(level, fieldNode, fieldNode, false, List.<JCAnnotation>nil(), List.<JCAnnotation>nil());
	}