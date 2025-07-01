def parse_s3_url(url):
    """
    Parses S3 URL.

    Returns bucket (domain) and file (full path).
    """
    bucket = ''
    path = ''
    if url:
        result = urlparse(url)
        bucket = result.netloc
        path = result.path.strip('/')
    return bucket, path