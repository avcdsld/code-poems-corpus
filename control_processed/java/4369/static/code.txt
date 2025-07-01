private void crossFirst1withNValues(final T1 val1, final T2 firstValN,
										final Iterator<T2> valsN, final FlatJoinFunction<T1, T2, O> joinFunction, final Collector<O> collector)
			throws Exception {
		T1 copy1 = createCopy(serializer1, val1, this.copy1);
		joinFunction.join(copy1, firstValN, collector);

		// set copy and join first element
		boolean more = true;
		do {
			final T2 nRec = valsN.next();

			if (valsN.hasNext()) {
				copy1 = createCopy(serializer1, val1, this.copy1);
				joinFunction.join(copy1, nRec, collector);
			} else {
				joinFunction.join(val1, nRec, collector);
				more = false;
			}
		}
		while (more);
	}