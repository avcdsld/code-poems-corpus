public static <X, P extends MessageQueryParameter<X>, R extends RequestBody, M extends MessageParameters> X getQueryParameter(
			final HandlerRequest<R, M> request,
			final Class<P> queryParameterClass) throws RestHandlerException {

		return getQueryParameter(request, queryParameterClass, null);
	}