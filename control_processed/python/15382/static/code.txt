def read_classification_results(storage_client, file_path):
  """Reads classification results from the file in Cloud Storage.

  This method reads file with classification results produced by running
  defense on singe batch of adversarial images.

  Args:
    storage_client: instance of CompetitionStorageClient or None for local file
    file_path: path of the file with results

  Returns:
    dictionary where keys are image names or IDs and values are classification
      labels
  """
  if storage_client:
    # file on Cloud
    success = False
    retry_count = 0
    while retry_count < 4:
      try:
        blob = storage_client.get_blob(file_path)
        if not blob:
          return {}
        if blob.size > MAX_ALLOWED_CLASSIFICATION_RESULT_SIZE:
          logging.warning('Skipping classification result because it''s too '
                          'big: %d bytes for %s', blob.size, file_path)
          return None
        buf = BytesIO()
        blob.download_to_file(buf)
        buf.seek(0)
        success = True
        break
      except Exception:
        retry_count += 1
        time.sleep(5)
    if not success:
      return None
  else:
    # local file
    try:
      with open(file_path, 'rb') as f:
        buf = BytesIO(f.read())
    except IOError:
      return None
  result = {}
  if PY3:
    buf = StringIO(buf.read().decode('UTF-8'))
  for row in csv.reader(buf):
    try:
      image_filename = row[0]
      if image_filename.endswith('.png') or image_filename.endswith('.jpg'):
        image_filename = image_filename[:image_filename.rfind('.')]
      label = int(row[1])
    except (IndexError, ValueError):
      continue
    result[image_filename] = label
  return result