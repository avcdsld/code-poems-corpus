def rank_reference_paragraphs(wiki_title, references_content, normalize=True):
  """Rank and return reference paragraphs by tf-idf score on title tokens."""
  normalized_title = _normalize_text(wiki_title)
  title_tokens = _tokens_to_score(
      set(tokenizer.encode(text_encoder.native_to_unicode(normalized_title))))
  ref_paragraph_info = []
  doc_counts = collections.defaultdict(int)
  for ref in references_content:
    for paragraph in ref.split("\n"):
      normalized_paragraph = _normalize_text(paragraph)
      if cc_utils.filter_paragraph(normalized_paragraph):
        # Skip paragraph
        continue
      counts = _token_counts(normalized_paragraph, title_tokens)
      for token in title_tokens:
        if counts[token]:
          doc_counts[token] += 1
      content = normalized_paragraph if normalize else paragraph
      info = {"content": content, "counts": counts}
      ref_paragraph_info.append(info)

  for info in ref_paragraph_info:
    score = 0.
    for token in title_tokens:
      term_frequency = info["counts"][token]
      inv_doc_frequency = (
          float(len(ref_paragraph_info)) / max(doc_counts[token], 1))
      score += term_frequency * math.log(inv_doc_frequency)
    info["score"] = score

  ref_paragraph_info.sort(key=lambda el: el["score"], reverse=True)
  return [info["content"] for info in ref_paragraph_info]