public static void keyPressWithShift(int key) {
		robot.keyPress(KeyEvent.VK_SHIFT);
		robot.keyPress(key);
		robot.keyRelease(key);
		robot.keyRelease(KeyEvent.VK_SHIFT);
		delay();
	}