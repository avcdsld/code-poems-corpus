function _scaleCanvas(ctx, params, transforms) {

	// Scale both the x- and y- axis using the 'scale' property
	if (params.scale !== 1) {
		params.scaleX = params.scaleY = params.scale;
	}

	// Scale canvas using shape as center of rotation
	ctx.translate(params.x, params.y);
	ctx.scale(params.scaleX, params.scaleY);
	ctx.translate(-params.x, -params.y);

	// If transformation data was given
	if (transforms) {
		// Update transformation data
		transforms.scaleX *= params.scaleX;
		transforms.scaleY *= params.scaleY;
	}
}