function invertCurve(curve){
		var out = new Array(curve.length);
		for (var j = 0; j < curve.length; j++){
			out[j] = 1 - curve[j];
		}
		return out;
	}