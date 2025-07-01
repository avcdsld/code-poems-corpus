function selectorsEqual (ruleA, ruleB) {
  return ruleA.selectors.some(sel => {
    return ruleB.selectors.some(s => s === sel)
  })
}