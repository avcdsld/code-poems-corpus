private void advanceTime(NFAState nfaState, long timestamp) throws Exception {
		try (SharedBufferAccessor<IN> sharedBufferAccessor = partialMatches.getAccessor()) {
			Collection<Tuple2<Map<String, List<IN>>, Long>> timedOut =
					nfa.advanceTime(sharedBufferAccessor, nfaState, timestamp);
			if (!timedOut.isEmpty()) {
				processTimedOutSequences(timedOut);
			}
		}
	}