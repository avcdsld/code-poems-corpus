private void processEvent(NFAState nfaState, IN event, long timestamp) throws Exception {
		try (SharedBufferAccessor<IN> sharedBufferAccessor = partialMatches.getAccessor()) {
			Collection<Map<String, List<IN>>> patterns =
				nfa.process(sharedBufferAccessor, nfaState, event, timestamp, afterMatchSkipStrategy, cepTimerService);
			processMatchedSequences(patterns, timestamp);
		}
	}