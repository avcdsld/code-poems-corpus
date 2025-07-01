@SuppressWarnings("unchecked")
	public static <X> X deserializeFunction(RuntimeContext context, byte[] serFun) throws FlinkException {
		if (!jythonInitialized) {
			// This branch is only tested by end-to-end tests
			String path = context.getDistributedCache().getFile(PythonConstants.FLINK_PYTHON_DC_ID).getAbsolutePath();

			String scriptName = PythonStreamExecutionEnvironment.PythonJobParameters.getScriptName(context.getExecutionConfig().getGlobalJobParameters());

			try {
				initPythonInterpreter(
					new String[]{Paths.get(path, scriptName).toString()},
					path,
					scriptName);
			} catch (Exception e) {

				try {
					LOG.error("Initialization of jython failed.", e);
					throw new FlinkRuntimeException("Initialization of jython failed.", e);
				} catch (Exception ie) {
					// this may occur if the initial exception relies on jython being initialized properly
					LOG.error("Initialization of jython failed. Could not print original stacktrace.", ie);
					throw new FlinkRuntimeException("Initialization of jython failed. Could not print original stacktrace.");
				}
			}
		}

		try {
			return (X) SerializationUtils.deserializeObject(serFun);
		} catch (IOException | ClassNotFoundException ex) {
			throw new FlinkException("Deserialization of user-function failed.", ex);
		}
	}