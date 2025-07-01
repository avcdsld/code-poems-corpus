private void fetchFilterSeeds() {
		if (seedList == null || seedList.isEmpty()) {
			return;
		}

		for (Iterator<URI> it = seedList.iterator(); it.hasNext();) {
			URI seed = it.next();
			for (FetchFilter filter : controller.getFetchFilters()) {
				FetchStatus filterReason = filter.checkFilter(seed);
				if (filterReason != FetchStatus.VALID) {
					if (log.isDebugEnabled()) {
						log.debug("Seed: " + seed + " was filtered with reason: " + filterReason);
					}
					it.remove();
					break;
				}
			}
		}
	}