def parse_timestamp(timestamp):
    """Parse ISO8601 timestamps given by github API."""
    dt = dateutil.parser.parse(timestamp)
    return dt.astimezone(dateutil.tz.tzutc())