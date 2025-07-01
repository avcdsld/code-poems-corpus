protected Connection createConnection(Socket socket, InputStream inputStream,
			OutputStream outputStream) throws IOException {
		return new Connection(socket, inputStream, outputStream);
	}