function processFallbackRules(root) {
  // an output for each execution mode

  // Reuse existing output in memory -- fixes issues with build "forgetting" about CSS vars previously working in IE 11 when compiling more than one thing at a time.
  if (!output) {
    output = {
      [ExecutionMode.CSS_COLOR]: [],
    };
  }

  // define which modes need to be processed
  const execModes = [ExecutionMode.CSS_COLOR];

  walkFallbackAtRules(root, execModes, output);
  walkFallbackRules(root, execModes, output);

  writeFallbackCSS(output);
}