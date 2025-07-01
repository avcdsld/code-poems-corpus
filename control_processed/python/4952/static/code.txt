def example_generator(all_files, urls_path, sum_token):
  """Generate examples."""

  def fix_run_on_sents(line):
    if u"@highlight" in line:
      return line
    if not line:
      return line
    if line[-1] in END_TOKENS:
      return line
    return line + u"."

  filelist = example_splits(urls_path, all_files)
  story_summary_split_token = u" <summary> " if sum_token else " "

  for story_file in filelist:
    story = []
    summary = []
    reading_highlights = False
    for line in tf.gfile.Open(story_file, "rb"):
      line = text_encoder.to_unicode_utf8(line.strip())
      line = fix_run_on_sents(line)
      if not line:
        continue
      elif line.startswith(u"@highlight"):
        if not story:
          break  # No article text.
        reading_highlights = True
      elif reading_highlights:
        summary.append(line)
      else:
        story.append(line)

    if (not story) or not summary:
      continue

    yield " ".join(story) + story_summary_split_token + " ".join(summary)