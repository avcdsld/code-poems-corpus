function _transformShape(canvas, ctx, params, width, height) {

	// Get conversion factor for radians
	params._toRad = (params.inDegrees ? (PI / 180) : 1);

	params._transformed = true;
	ctx.save();

	// Optionally measure (x, y) position from top-left corner
	if (!params.fromCenter && !params._centered && width !== undefined) {
		// Always draw from center unless otherwise specified
		if (height === undefined) {
			height = width;
		}
		params.x += width / 2;
		params.y += height / 2;
		params._centered = true;
	}
	// Optionally rotate shape
	if (params.rotate) {
		_rotateCanvas(ctx, params, null);
	}
	// Optionally scale shape
	if (params.scale !== 1 || params.scaleX !== 1 || params.scaleY !== 1) {
		_scaleCanvas(ctx, params, null);
	}
	// Optionally translate shape
	if (params.translate || params.translateX || params.translateY) {
		_translateCanvas(ctx, params, null);
	}

}