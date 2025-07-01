private <X> DataSource<X> fromParallelCollection(SplittableIterator<X> iterator, TypeInformation<X> type, String callLocationName) {
		return new DataSource<>(this, new ParallelIteratorInputFormat<>(iterator), type, callLocationName);
	}