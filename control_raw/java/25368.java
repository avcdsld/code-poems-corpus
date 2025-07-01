private boolean checkFileNHeader(final InputStream is, final StreamParseWriter dout, StreamData din, int cidx)
          throws IOException {
    byte[] headerBytes = ZipUtil.unzipForHeader(din.getChunkData(cidx), this._setup._chunk_size);
    ParseSetup ps = ParseSetup.guessSetup(null, headerBytes, new ParseSetup(GUESS_INFO, ParseSetup.GUESS_SEP,
            this._setup._single_quotes, ParseSetup.GUESS_HEADER, ParseSetup.GUESS_COL_CNT, null, null));
    // check to make sure datasets in file belong to the same dataset
    // just check for number for number of columns/separator here.  Ignore the column type, user can force it
    if ((this._setup._number_columns != ps._number_columns) || (this._setup._separator != ps._separator)) {
      String warning = "Your zip file contains a file that belong to another dataset with different " +
              "number of column or separator.  Number of columns for files that have been parsed = "+
              this._setup._number_columns + ".  Number of columns in new file = "+ps._number_columns+
              ".  This new file is skipped and not parsed.";
      dout.addError(new ParseWriter.ParseErr(warning, -1, -1L, -2L));
      // something is wrong
      return false;
    } else {
      // assume column names must appear in the first file.  If column names appear in first and other
      // files, they will be recognized.  Otherwise, if no column name ever appear in the first file, the other
      // column names in the other files will not be recognized.
      if (ps._check_header == ParseSetup.HAS_HEADER) {
        if (this._setup._column_names != null) {
          // found header in later files, only incorporate it if the column names are the same as before
          String[] thisColumnName = this._setup.getColumnNames();
          String[] psColumnName = ps.getColumnNames();
          Boolean sameColumnNames = true;
          for (int index = 0; index < this._setup._number_columns; index++) {
            if (!(thisColumnName[index].equals(psColumnName[index]))) {
              sameColumnNames = false;
              break;
            }
          }
          if (sameColumnNames)  // only recognize current file header if it has the same column names as previous files
            this._setup.setCheckHeader(ps._check_header);
        }
      } else  // should refresh _setup with correct check_header
        this._setup.setCheckHeader(ps._check_header);
    }
    return true;  // everything is fine
  }