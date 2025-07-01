@VisibleForTesting
	List<Container> getContainersFromPreviousAttemptsUnsafe(final Object response) {
		if (method != null && response != null) {
			try {
				@SuppressWarnings("unchecked")
				final List<Container> containers = (List<Container>) method.invoke(response);
				if (containers != null && !containers.isEmpty()) {
					return containers;
				}
			} catch (Exception t) {
				logger.error("Error invoking 'getContainersFromPreviousAttempts()'", t);
			}
		}

		return Collections.emptyList();
	}