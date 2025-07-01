function _getBioContent (el, importer) {
  let $$ = el.createElement.bind(el.getOwnerDocument())
  let bioEl = findChild(el, 'bio')

  // If there is no bio element we should provide it
  if (!bioEl) {
    bioEl = $$('bio')
  }

  // TODO: this code looks similar to what we have in abstract or and caption
  // drop everything other than 'p' from bio
  retainChildren(bioEl, 'p')
  // there must be at least one paragraph
  if (!bioEl.find('p')) {
    bioEl.append($$('p'))
  }

  return bioEl.children.map(child => importer.convertElement(child).id)
}