public AnnotationMetadata buildDeclared(T element) {
        final AnnotationMetadata existing = MUTATED_ANNOTATION_METADATA.get(element);
        if (existing != null) {
            return existing;
        } else {

            DefaultAnnotationMetadata annotationMetadata = new DefaultAnnotationMetadata();

            try {
                AnnotationMetadata metadata = buildInternal(null, element, annotationMetadata, true, true);
                if (metadata.isEmpty()) {
                    return AnnotationMetadata.EMPTY_METADATA;
                }
                return metadata;
            } catch (RuntimeException e) {
                if ("org.eclipse.jdt.internal.compiler.problem.AbortCompilation".equals(e.getClass().getName())) {
                    // workaround for a bug in the Eclipse APT implementation. See bug 541466 on their Bugzilla.
                    return AnnotationMetadata.EMPTY_METADATA;
                } else {
                    throw e;
                }
            }
        }
    }