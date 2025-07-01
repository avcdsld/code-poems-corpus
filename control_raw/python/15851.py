def FromDatetime(self, dt):
    """Converts datetime to Timestamp."""
    td = dt - datetime(1970, 1, 1)
    self.seconds = td.seconds + td.days * _SECONDS_PER_DAY
    self.nanos = td.microseconds * _NANOS_PER_MICROSECOND