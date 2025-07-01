function run() {
	return Promise.resolve()
		.then(loadEnvFile)
		.then(loadConfigFile)
		.then(mergeOptions)
		.then(startBroker)
		.catch(err => {
			logger.error(err);
			process.exit(1);
		});
}