function getFunctionCallType (func) {
  if (!(isExternalDirectCall(func) || isThisLocalCall(func) || isSuperLocalCall(func) || isLocalCall(func) || isLibraryCall(func))) throw new Error('staticAnalysisCommon.js: not function call Node')
  if (isExternalDirectCall(func) || isThisLocalCall(func) || isSuperLocalCall(func) || isLibraryCall(func)) return func.attributes.type
  return findFirstSubNodeLTR(func, exactMatch(nodeTypes.IDENTIFIER)).attributes.type
}