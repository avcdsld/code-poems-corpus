function focusToFirstTh(sq, $table) {
  const range = sq.getSelection();

  range.selectNodeContents($table.find('th')[0]);
  range.collapse(true);
  sq.setSelection(range);
}