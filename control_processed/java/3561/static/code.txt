public W addWindow(W newWindow, MergeFunction<W> mergeFunction) throws Exception {

		List<W> windows = new ArrayList<>();

		windows.addAll(this.mapping.keySet());
		windows.add(newWindow);

		final Map<W, Collection<W>> mergeResults = new HashMap<>();
		windowAssigner.mergeWindows(windows,
				new MergingWindowAssigner.MergeCallback<W>() {
					@Override
					public void merge(Collection<W> toBeMerged, W mergeResult) {
						if (LOG.isDebugEnabled()) {
							LOG.debug("Merging {} into {}", toBeMerged, mergeResult);
						}
						mergeResults.put(mergeResult, toBeMerged);
					}
				});

		W resultWindow = newWindow;
		boolean mergedNewWindow = false;

		// perform the merge
		for (Map.Entry<W, Collection<W>> c: mergeResults.entrySet()) {
			W mergeResult = c.getKey();
			Collection<W> mergedWindows = c.getValue();

			// if our new window is in the merged windows make the merge result the
			// result window
			if (mergedWindows.remove(newWindow)) {
				mergedNewWindow = true;
				resultWindow = mergeResult;
			}

			// pick any of the merged windows and choose that window's state window
			// as the state window for the merge result
			W mergedStateWindow = this.mapping.get(mergedWindows.iterator().next());

			// figure out the state windows that we are merging
			List<W> mergedStateWindows = new ArrayList<>();
			for (W mergedWindow: mergedWindows) {
				W res = this.mapping.remove(mergedWindow);
				if (res != null) {
					mergedStateWindows.add(res);
				}
			}

			this.mapping.put(mergeResult, mergedStateWindow);

			// don't put the target state window into the merged windows
			mergedStateWindows.remove(mergedStateWindow);

			// don't merge the new window itself, it never had any state associated with it
			// i.e. if we are only merging one pre-existing window into itself
			// without extending the pre-existing window
			if (!(mergedWindows.contains(mergeResult) && mergedWindows.size() == 1)) {
				mergeFunction.merge(mergeResult,
						mergedWindows,
						this.mapping.get(mergeResult),
						mergedStateWindows);
			}
		}

		// the new window created a new, self-contained window without merging
		if (mergeResults.isEmpty() || (resultWindow.equals(newWindow) && !mergedNewWindow)) {
			this.mapping.put(resultWindow, resultWindow);
		}

		return resultWindow;
	}