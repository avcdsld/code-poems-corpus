function GridFSBucketReadStream(chunks, files, readPreference, filter, options) {
  this.s = {
    bytesRead: 0,
    chunks: chunks,
    cursor: null,
    expected: 0,
    files: files,
    filter: filter,
    init: false,
    expectedEnd: 0,
    file: null,
    options: options,
    readPreference: readPreference
  };

  stream.Readable.call(this);
}