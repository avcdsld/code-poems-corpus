function writeNotes() {
  let output = '';
  let compatNotes = collectCompatNotes();
  for (let note of compatNotes) {
    let noteIndex = compatNotes.indexOf(note);
    output += `<p id=compatNote_${noteIndex+1}>${noteIndex+1}. ${note}</p>`;
  }
  return output;
}