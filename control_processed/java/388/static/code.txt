private boolean hasLombokPublicAccessor(MetadataGenerationEnvironment env,
			boolean getter) {
		String annotation = (getter ? LOMBOK_GETTER_ANNOTATION
				: LOMBOK_SETTER_ANNOTATION);
		AnnotationMirror lombokMethodAnnotationOnField = env.getAnnotation(getField(),
				annotation);
		if (lombokMethodAnnotationOnField != null) {
			return isAccessLevelPublic(env, lombokMethodAnnotationOnField);
		}
		AnnotationMirror lombokMethodAnnotationOnElement = env
				.getAnnotation(getOwnerElement(), annotation);
		if (lombokMethodAnnotationOnElement != null) {
			return isAccessLevelPublic(env, lombokMethodAnnotationOnElement);
		}
		return (env.getAnnotation(getOwnerElement(), LOMBOK_DATA_ANNOTATION) != null);
	}