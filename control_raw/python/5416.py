def file_page_generator(my_file, max_page_size=2**28):
  """Read wikipedia pages from a history dump.

  Since some pages can be terabytes in size (with all the revisions),
  we limit page size to max_page_size bytes.

  Args:
    my_file: an open file object.
    max_page_size: an integer

  Yields:
    strings
  """
  page_start = "  <page>\n"
  page_end = "  </page>\n"
  chunk_size = max_page_size
  page_start = "  <page>\n"
  page_end = "  </page>\n"
  leftovers = ""
  while True:
    chunk = my_file.read(chunk_size)
    if not chunk:
      break
    chunk = leftovers + chunk
    current_pos = 0
    while True:
      start_pos = chunk.find(page_start, current_pos)
      if start_pos == -1:
        break
      end_pos = chunk.find(page_end, start_pos)
      if end_pos == -1:
        if len(chunk) - start_pos > max_page_size:
          leftovers = ""
        else:
          leftovers = chunk[start_pos:]
        break
      raw_page = chunk[start_pos + len(page_start):end_pos]
      if len(raw_page) < max_page_size:
        ret = parse_page(raw_page)
        if ret:
          yield ret
      current_pos = end_pos + len(page_end)