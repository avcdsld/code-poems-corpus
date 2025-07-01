public static void scale(File srcImageFile, File destImageFile, int width, int height, Color fixedColor) throws IORuntimeException {
		write(scale(read(srcImageFile), width, height, fixedColor), destImageFile);
	}