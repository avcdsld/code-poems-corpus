function next(cursor, callback) {
  // Return the currentDoc if someone called hasNext first
  if (cursor.s.currentDoc) {
    const doc = cursor.s.currentDoc;
    cursor.s.currentDoc = null;
    return callback(null, doc);
  }

  // Return the next object
  nextObject(cursor, callback);
}