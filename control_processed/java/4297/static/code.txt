public static Environment merge(Environment env1, Environment env2) {
		final Environment mergedEnv = new Environment();

		// merge tables
		final Map<String, TableEntry> tables = new LinkedHashMap<>(env1.getTables());
		tables.putAll(env2.getTables());
		mergedEnv.tables = tables;

		// merge functions
		final Map<String, FunctionEntry> functions = new HashMap<>(env1.getFunctions());
		functions.putAll(env2.getFunctions());
		mergedEnv.functions = functions;

		// merge execution properties
		mergedEnv.execution = ExecutionEntry.merge(env1.getExecution(), env2.getExecution());

		// merge deployment properties
		mergedEnv.deployment = DeploymentEntry.merge(env1.getDeployment(), env2.getDeployment());

		return mergedEnv;
	}