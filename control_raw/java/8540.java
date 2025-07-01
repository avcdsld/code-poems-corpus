@Override
	public boolean cd(String directory) {
		boolean flag = true;
		try {
			flag = client.changeWorkingDirectory(directory);
		} catch (IOException e) {
			throw new FtpException(e);
		}
		return flag;
	}