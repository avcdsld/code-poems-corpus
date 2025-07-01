private void crossSecond1withNValues(T2 val1, T1 firstValN,
										Iterator<T1> valsN, FlatJoinFunction<T1, T2, O> joinFunction, Collector<O> collector) throws Exception {
		T2 copy2 = createCopy(serializer2, val1, this.copy2);
		joinFunction.join(firstValN, copy2, collector);

		// set copy and join first element
		boolean more = true;
		do {
			final T1 nRec = valsN.next();

			if (valsN.hasNext()) {
				copy2 = createCopy(serializer2, val1, this.copy2);
				joinFunction.join(nRec, copy2, collector);
			} else {
				joinFunction.join(nRec, val1, collector);
				more = false;
			}
		}
		while (more);
	}