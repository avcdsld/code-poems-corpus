function focusToCell(sq, range, targetCell) {
  range.selectNodeContents(targetCell);
  range.collapse(true);
  sq.setSelection(range);
}