public Invocable invokeScript(ScriptWrapper script) throws ScriptException {
		logger.debug("invokeScript " + script.getName());
		preInvokeScript(script);

		ClassLoader previousContextClassLoader = Thread.currentThread().getContextClassLoader();
		Thread.currentThread().setContextClassLoader(ExtensionFactory.getAddOnLoader());
		try {
			return invokeScriptImpl(script);
		} finally {
			Thread.currentThread().setContextClassLoader(previousContextClassLoader);
		}
	}