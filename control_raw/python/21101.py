def ListDirectoryAbsolute(directory):
  """Yields all files in the given directory. The paths are absolute."""
  return (os.path.join(directory, path)
          for path in tf.io.gfile.listdir(directory))