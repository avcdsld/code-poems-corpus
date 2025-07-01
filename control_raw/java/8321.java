public static URLEncoder createDefault() {
		final URLEncoder encoder = new URLEncoder();
		encoder.addSafeCharacter('-');
		encoder.addSafeCharacter('.');
		encoder.addSafeCharacter('_');
		encoder.addSafeCharacter('~');
		// Add the sub-delims
		encoder.addSafeCharacter('!');
		encoder.addSafeCharacter('$');
		encoder.addSafeCharacter('&');
		encoder.addSafeCharacter('\'');
		encoder.addSafeCharacter('(');
		encoder.addSafeCharacter(')');
		encoder.addSafeCharacter('*');
		encoder.addSafeCharacter('+');
		encoder.addSafeCharacter(',');
		encoder.addSafeCharacter(';');
		encoder.addSafeCharacter('=');
		// Add the remaining literals
		encoder.addSafeCharacter(':');
		encoder.addSafeCharacter('@');
		// Add '/' so it isn't encoded when we encode a path
		encoder.addSafeCharacter('/');

		return encoder;
	}