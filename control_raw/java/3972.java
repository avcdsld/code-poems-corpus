private void retractRecordWithRowNumber(
			SortedMap<BaseRow, Long> sortedMap, BaseRow sortKey, BaseRow inputRow, Collector<BaseRow> out)
			throws Exception {
		Iterator<Map.Entry<BaseRow, Long>> iterator = sortedMap.entrySet().iterator();
		long curRank = 0L;
		boolean findsSortKey = false;
		while (iterator.hasNext() && isInRankEnd(curRank)) {
			Map.Entry<BaseRow, Long> entry = iterator.next();
			BaseRow key = entry.getKey();
			if (!findsSortKey && key.equals(sortKey)) {
				List<BaseRow> inputs = dataState.get(key);
				if (inputs == null) {
					// Skip the data if it's state is cleared because of state ttl.
					if (lenient) {
						LOG.warn(STATE_CLEARED_WARN_MSG);
					} else {
						throw new RuntimeException(STATE_CLEARED_WARN_MSG);
					}
				} else {
					Iterator<BaseRow> inputIter = inputs.iterator();
					while (inputIter.hasNext() && isInRankEnd(curRank)) {
						curRank += 1;
						BaseRow prevRow = inputIter.next();
						if (!findsSortKey && equaliser.equalsWithoutHeader(prevRow, inputRow)) {
							delete(out, prevRow, curRank);
							curRank -= 1;
							findsSortKey = true;
							inputIter.remove();
						} else if (findsSortKey) {
							retract(out, prevRow, curRank + 1);
							collect(out, prevRow, curRank);
						}
					}
					if (inputs.isEmpty()) {
						dataState.remove(key);
					} else {
						dataState.put(key, inputs);
					}
				}
			} else if (findsSortKey) {
				List<BaseRow> inputs = dataState.get(key);
				int i = 0;
				while (i < inputs.size() && isInRankEnd(curRank)) {
					curRank += 1;
					BaseRow prevRow = inputs.get(i);
					retract(out, prevRow, curRank + 1);
					collect(out, prevRow, curRank);
					i++;
				}
			} else {
				curRank += entry.getValue();
			}
		}
	}