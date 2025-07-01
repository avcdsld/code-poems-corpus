public static void deleteFileOrDirectory(File file) {
    if (!file.isDirectory()) {
      file.delete();
      return;
    }

    if (file.list().length == 0) { //Nothing under directory. Just delete it.
      file.delete();
      return;
    }

    for (String temp : file.list()) { //Delete files or directory under current directory.
      File fileDelete = new File(file, temp);
      deleteFileOrDirectory(fileDelete);
    }
    //Now there is nothing under directory, delete it.
    deleteFileOrDirectory(file);
  }