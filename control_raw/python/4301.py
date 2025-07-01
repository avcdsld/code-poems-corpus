def _page_to_title(page):
  """Extract the title from a page.

  Args:
    page: a unicode string
  Returns:
    a unicode string
  """
  # print("page=%s" % page)
  start_tag = u"<title>"
  end_tag = u"</title>"
  start_pos = page.find(start_tag)
  end_pos = page.find(end_tag)
  assert start_pos != -1
  assert end_pos != -1
  start_pos += len(start_tag)
  return page[start_pos:end_pos]