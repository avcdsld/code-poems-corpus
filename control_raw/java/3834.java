@Override
	public void open(FileInputSplit split) throws IOException {
		super.open(split);
		initBuffers();

		this.offset = splitStart;
		if (this.splitStart != 0) {
			this.stream.seek(offset);
			readLine();
			// if the first partial record already pushes the stream over
			// the limit of our split, then no record starts within this split
			if (this.overLimit) {
				this.end = true;
			}
		} else {
			fillBuffer(0);
		}
	}