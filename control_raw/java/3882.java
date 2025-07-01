private void writeObject(ObjectOutputStream out) throws IOException {
		super.write(out);
		out.writeUTF(mapredOutputFormat.getClass().getName());
		jobConf.write(out);
	}