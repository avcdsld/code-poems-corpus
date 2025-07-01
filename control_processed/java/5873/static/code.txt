public int sendBuffer2(SingleElementPushBackIterator<IN2> input) throws IOException {
		if (serializer2 == null) {
			IN2 value = input.next();
			serializer2 = getSerializer(value);
			input.pushBack(value);
		}
		return sendBuffer(input, serializer2);
	}