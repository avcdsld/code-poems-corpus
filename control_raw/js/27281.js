function isPathLayer(layer) {
	var method = layer._method;
	return (method === $.fn.drawLine || method === $.fn.drawQuadratic || method === $.fn.drawBezier);
}