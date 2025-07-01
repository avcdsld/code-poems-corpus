def get_url(params):
    """Return external URL for warming up a given chart/table cache."""
    baseurl = 'http://{SUPERSET_WEBSERVER_ADDRESS}:{SUPERSET_WEBSERVER_PORT}/'.format(
        **app.config)
    with app.test_request_context():
        return urllib.parse.urljoin(
            baseurl,
            url_for('Superset.explore_json', **params),
        )