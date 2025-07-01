function processLeaves(leaf) {
  /**
   * Get an array of the mark types, converted to their MDAST equivalent
   * types.
   */
  const { marks = [], text } = leaf;
  const markTypes = marks.map(mark => markMap[mark.type]);

  if (typeof leaf.text === 'string') {
    /**
     * Code marks must be removed from the marks array, and the presence of a
     * code mark changes the text node type that should be used.
     */
    const { filteredMarkTypes, textNodeType } = processCodeMark(markTypes);
    return { text, marks: filteredMarkTypes, textNodeType };
  }

  return { node: leaf.node, marks: markTypes };
}