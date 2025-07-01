@Override
	public boolean callWithNextKey(final FlatJoinFunction<T1, T2, O> joinFunction, final Collector<O> collector)
			throws Exception {
		if (!this.iterator1.nextKey() || !this.iterator2.nextKey()) {
			// consume all remaining keys (hack to prevent remaining inputs during iterations, lets get rid of this soon)
			while (this.iterator1.nextKey()) {
			}
			while (this.iterator2.nextKey()) {
			}

			return false;
		}

		final TypePairComparator<T1, T2> comparator = this.pairComparator;
		comparator.setReference(this.iterator1.getCurrent());
		T2 current2 = this.iterator2.getCurrent();

		// zig zag
		while (true) {
			// determine the relation between the (possibly composite) keys
			final int comp = comparator.compareToReference(current2);

			if (comp == 0) {
				break;
			}

			if (comp < 0) {
				if (!this.iterator2.nextKey()) {
					return false;
				}
				current2 = this.iterator2.getCurrent();
			} else {
				if (!this.iterator1.nextKey()) {
					return false;
				}
				comparator.setReference(this.iterator1.getCurrent());
			}
		}

		// here, we have a common key! call the join function with the cross product of the
		// values
		final Iterator<T1> values1 = this.iterator1.getValues();
		final Iterator<T2> values2 = this.iterator2.getValues();

		crossMatchingGroup(values1, values2, joinFunction, collector);
		return true;
	}