function focusToNextCell(sq, $cell) {
  const range = sq.getSelection();

  range.selectNodeContents($cell.next()[0]);
  range.collapse(true);

  sq.setSelection(range);
}