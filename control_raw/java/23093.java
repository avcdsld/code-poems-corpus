public String attachToGetConnectorAddress() throws Exception {
		VirtualMachine vm = null;

		// 1. attach vm
		vm = VirtualMachine.attach(pid);

		try {
			// 2. 检查smartAgent是否已启动
			Properties agentProps = vm.getAgentProperties();
			String address = (String) agentProps.get(LOCAL_CONNECTOR_ADDRESS_PROP);

			if (address != null) {
				return address;
			}

			// 3. 未启动，尝试启动
			String home = vm.getSystemProperties().getProperty("java.home");

			// Normally in ${java.home}/jre/lib/management-agent.jar but might
			// be in ${java.home}/lib in build environments.

			String agentPath = home + File.separator + "jre" + File.separator + "lib" + File.separator
					+ "management-agent.jar";
			File f = new File(agentPath);
			if (!f.exists()) {
				agentPath = home + File.separator + "lib" + File.separator + "management-agent.jar";
				f = new File(agentPath);
				if (!f.exists()) {
					throw new IOException("Management agent not found");
				}
			}

			agentPath = f.getCanonicalPath();
			vm.loadAgent(agentPath, "com.sun.management.jmxremote");

			// 4. 再次获取connector address
			agentProps = vm.getAgentProperties();
			address = (String) agentProps.get(LOCAL_CONNECTOR_ADDRESS_PROP);

			if (address == null) {
				throw new IOException("Fails to find connector address");
			}

			return address;
		} finally {
			vm.detach();
		}
	}