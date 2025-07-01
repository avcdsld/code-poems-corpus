public void setValue(CharBuffer buffer) {
		checkNotNull(buffer);
		final int len = buffer.length();
		ensureSize(len);
		buffer.get(this.value, 0, len);
		this.len = len;
		this.hashCode = 0;
	}