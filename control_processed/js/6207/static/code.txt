function pushNode(result, nodes) {
	'use strict';

	var temp;

	if (result.length === 0) {
		return nodes;
	}
	if (result.length < nodes.length) {
		// switch so the comparison is shortest
		temp = result;
		result = nodes;
		nodes = temp;
	}
	for (var i = 0, l = nodes.length; i < l; i++) {
		if (!result.includes(nodes[i])) {
			result.push(nodes[i]);
		}
	}
	return result;
}