def read_url(url):
    """Reads given URL as JSON and returns data as loaded python object."""
    logging.debug('reading {url} ...'.format(url=url))
    token = os.environ.get("BOKEH_GITHUB_API_TOKEN")
    headers = {}
    if token:
        headers['Authorization'] = 'token %s' % token
    request = Request(url, headers=headers)
    response = urlopen(request).read()
    return json.loads(response.decode("UTF-8"))