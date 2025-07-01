function normalizeSource(
  source /*: string */,
  map /*: BabelSourceMap */,
) /*: string */ {
  const {sourceRoot} = map;
  source = String(source);
  // Some source maps produce relative source paths like "./foo.js" instead of
  // "foo.js".  Normalize these first so that future comparisons will succeed.
  // See bugzil.la/1090768.
  source = util.normalize(source);
  // Always ensure that absolute sources are internally stored relative to
  // the source root, if the source root is absolute. Not doing this would
  // be particularly problematic when the source root is a prefix of the
  // source (valid, but why??). See github issue #199 and bugzil.la/1188982.
  source =
    sourceRoot && util.isAbsolute(sourceRoot) && util.isAbsolute(source)
      ? util.relative(sourceRoot, source)
      : source;

  return source;
}