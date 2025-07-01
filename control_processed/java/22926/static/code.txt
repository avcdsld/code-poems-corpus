@SuppressWarnings("unchecked") public Class<T> getAnnotationHandledByThisHandler() {
		return (Class<T>) SpiLoadUtil.findAnnotationClass(getClass(), EclipseAnnotationHandler.class);
	}