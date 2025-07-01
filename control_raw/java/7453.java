public Img pressImage(Image pressImg, int x, int y, float alpha) {
		final int pressImgWidth = pressImg.getWidth(null);
		final int pressImgHeight = pressImg.getHeight(null);

		return pressImage(pressImg, new Rectangle(x, y, pressImgWidth, pressImgHeight), alpha);
	}