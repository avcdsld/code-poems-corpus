function getEntries(props, entries, indexes) {
  const { onDOMNodeMouseOver, onDOMNodeMouseOut, onInspectIconClick } = props;

  // Make indexes ordered by ascending.
  indexes.sort(function(a, b) {
    return a - b;
  });

  return indexes.map((index, i) => {
    const [key, entryValue] = entries[index];
    const value =
      entryValue.value !== undefined ? entryValue.value : entryValue;

    return PropRep({
      name: key,
      equal: " \u2192 ",
      object: value,
      mode: MODE.TINY,
      onDOMNodeMouseOver,
      onDOMNodeMouseOut,
      onInspectIconClick
    });
  });
}