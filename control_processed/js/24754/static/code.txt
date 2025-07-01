function isDirectionLTR(
  str: string,
  strongFallback: ?BidiDirection,
): boolean {
  return getDirection(str, strongFallback) === UnicodeBidiDirection.LTR;
}