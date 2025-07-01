public void printTopStack() throws IOException {
		System.out.printf("%n Stack trace of top %d threads:%n", view.threadLimit);

		ThreadInfo[] infos = view.topThreadInfo.getTopThreadInfo();
		for (ThreadInfo info : infos) {
			if (info == null) {
				continue;
			}
			printSingleThread(info);
		}
		System.out.flush();
	}