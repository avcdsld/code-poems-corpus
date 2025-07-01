function inlineMargins ($) {
  $('table[style*=margin]').toNodes().forEach(($el) => {
    const { left, right } = getSideMargins($el.attr('style'))

    if (left === 'auto' && right === 'auto') {
      $el.attr('align', 'center')
    } else if (left === 'auto' && right !== 'auto') {
      $el.attr('align', 'right')
    } else if (left !== 'auto') {
      $el.attr('align', 'left')
    }
  })
}