function parseDate(str/*:string|Date*/, fixdate/*:?number*/)/*:Date*/ {
	var d = new Date(str);
	if(good_pd) {
		/*:: if(fixdate == null) fixdate = 0; */
		if(fixdate > 0) d.setTime(d.getTime() + d.getTimezoneOffset() * 60 * 1000);
		else if(fixdate < 0) d.setTime(d.getTime() - d.getTimezoneOffset() * 60 * 1000);
		return d;
	}
	if(str instanceof Date) return str;
	if(good_pd_date.getFullYear() == 1917 && !isNaN(d.getFullYear())) {
		var s = d.getFullYear();
		if(str.indexOf("" + s) > -1) return d;
		d.setFullYear(d.getFullYear() + 100); return d;
	}
	var n = str.match(/\d+/g)||["2017","2","19","0","0","0"];
	var out = new Date(+n[0], +n[1] - 1, +n[2], (+n[3]||0), (+n[4]||0), (+n[5]||0));
	if(str.indexOf("Z") > -1) out = new Date(out.getTime() - out.getTimezoneOffset() * 60 * 1000);
	return out;
}