public <A extends Annotation> A annotation(Class<A> annotationClass) {
        return field.getAnnotation(annotationClass);
    }