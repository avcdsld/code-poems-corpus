public void stop()
			throws MojoExecutionException, IOException, InstanceNotFoundException {
		try {
			this.connection.invoke(this.objectName, "shutdown", null, null);
		}
		catch (ReflectionException ex) {
			throw new MojoExecutionException("Shutdown failed", ex.getCause());
		}
		catch (MBeanException ex) {
			throw new MojoExecutionException("Could not invoke shutdown operation", ex);
		}
	}