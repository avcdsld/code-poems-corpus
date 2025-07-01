function white() {
		var c = walker.ch,
			token = '';
	
		while (c === " " || c === "\t") {
			token += c;
			c = walker.nextChar();
		}
	
		tokener(token, 'white');
	
	}