function drawRadialUnits(context, options) {
    if (!options.units) return;

    context.save();
    context.font = drawings.font(options, 'Units', context.max / 200);
    context.fillStyle = options.colorUnits;
    context.textAlign = 'center';
    context.fillText(options.units, 0, context.max / 3.25, context.max * 0.8);
    context.restore();
}