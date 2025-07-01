function headerQuickLinkReplacer(fullMatch, openingTag, headerId, remainingHtml, headerText) {
  const link = makeLink(headerId, headerText);
  return `${openingTag} class="quick-link quick-link__container">${link}${remainingHtml}`;
}