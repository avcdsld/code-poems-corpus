def finish(self):
    """Finishes transconding and returns the video.

    Returns:
      bytes

    Raises:
      IOError: in case of transcoding error.
    """
    if self.proc is None:
      return None
    self.proc.stdin.close()
    for thread in (self._out_thread, self._err_thread):
      thread.join()
    (out, err) = [
        b"".join(chunks) for chunks in (self._out_chunks, self._err_chunks)
    ]
    self.proc.stdout.close()
    self.proc.stderr.close()
    if self.proc.returncode:
      err = "\n".join([" ".join(self.cmd), err.decode("utf8")])
      raise IOError(err)
    del self.proc
    self.proc = None
    return out