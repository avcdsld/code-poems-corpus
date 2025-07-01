function benchmark(fn, times, name){
	fn = fn.toString();
	var s = fn.indexOf('{')+1,
		e = fn.lastIndexOf('}');
	fn = fn.substring(s,e);

	return benchmarkString(fn, times, name);
}