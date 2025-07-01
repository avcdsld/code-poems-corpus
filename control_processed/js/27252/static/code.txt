function ParseError(message, start, end, next) {
	this.message = message;
	this.start = start;
	this.end = end;
	this.next = next;
}