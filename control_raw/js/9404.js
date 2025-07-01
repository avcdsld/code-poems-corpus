function circuitClose(item) {
		item.state = C.CIRCUIT_CLOSE;
		item.ep.state = true;
		item.failures = 0;
		item.count = 0;

		logger.debug(`Circuit breaker has been closed on '${item.ep.name}' endpoint.`, { nodeID: item.ep.id, action: item.ep.action.name });

		broker.broadcast("$circuit-breaker.closed", { nodeID: item.ep.id, action: item.ep.action.name });

		if (item.cbTimer) {
			clearTimeout(item.cbTimer);
			item.cbTimer = null;
		}
	}