function translateColor(colorArr, variationName, execMode) {
  const [colorVar, alpha] = colorArr;

  // returns the real color representation
  if (!options.palette) {
    options.palette = getColorPalette();
  }

  const underlineColor = options.palette[variationName][colorVar];

  if (!underlineColor) {
    // variable is not mandatory in non-default variations
    if (variationName !== defaultVariation) {
      return null;
    }
    throw new Error(
      `The variable name '${colorVar}' doesn't exists in your palette.`,
    );
  }

  switch (execMode) {
    case ExecutionMode.CSS_COLOR:
      // with default alpha - just returns the color
      if (alpha === '1') {
        return rgb2hex(underlineColor).hex;
      }
      // with custom alpha, convert it to rgba
      const rgbaColor = hexToRgba(rgb2hex(underlineColor).hex, alpha);
      return rgbaColor;
    default:
      if (alpha === 1) {
        return `rgba(var(--bolt-theme-${colorVar}), ${alpha})`;
        //return `var(--bolt-theme-${colorVar})`; // @todo: re-evaluate if hex values should ever get outputted here
      } else {
        return `rgba(var(--bolt-theme-${colorVar}), ${alpha})`;
      }
  }
}