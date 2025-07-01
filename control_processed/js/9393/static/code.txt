function startWorkers(instances) {
	let stopping = false;

	cluster.on("exit", function(worker, code) {
		if (!stopping) {
			// only restart the worker if the exit was by an error
			if (production && code !== 0) {
				logger.info(`The worker #${worker.id} has disconnected`);
				logger.info(`Worker #${worker.id} restarting...`);
				cluster.fork();
				logger.info(`Worker #${worker.id} restarted`);
			} else {
				process.exit(code);
			}
		}
	});

	const workerCount = Number.isInteger(instances) && instances > 0 ? instances : os.cpus().length;

	logger.info(`Starting ${workerCount} workers...`);

	for (let i = 0; i < workerCount; i++) {
		cluster.fork();
	}

	stopSignals.forEach(function (signal) {
		process.on(signal, () => {
			logger.info(`Got ${signal}, stopping workers...`);
			stopping = true;
			cluster.disconnect(function () {
				logger.info("All workers stopped, exiting.");
				process.exit(0);
			});
		});
	});
}