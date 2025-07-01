def _encode_wiki_sections(sections, vocab):
  """Encodes sections with vocab. Returns ids and section boundaries."""
  ids = []
  section_boundaries = []
  for i, section in enumerate(sections):
    if i > 0:
      # Skip including article title
      ids.extend(vocab.encode(_format_title(_normalize_text(section.title))))
    ids.extend(vocab.encode(_normalize_text(section.text)))
    section_boundaries.append(len(ids))

  return ids, section_boundaries