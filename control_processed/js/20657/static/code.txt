function createChangeEvent (selected, selection, markdown, native, html) {
  if (typeof selected !== 'string') {
    throw new TypeError('The selected content value must be a string.')
  }

  if (typeof selection !== 'object') {
    throw new TypeError('The selection must be an object.')
  }

  if (typeof selection.start !== 'number') {
    throw new TypeError('The selection start value must be a number.')
  }

  if (typeof selection.end !== 'number') {
    throw new TypeError('The selection end value must be a number.')
  }

  if (typeof markdown !== 'string') {
    throw new TypeError('The markdown content value must be a string.')
  }

  if (typeof native !== 'object') {
    throw new TypeError('The native event must be an object.')
  }

  if (typeof html !== 'string') {
    throw new TypeError('The html content value must be a string.')
  }

  return {
    selected,
    selection,
    markdown,
    native,
    html
  }
}