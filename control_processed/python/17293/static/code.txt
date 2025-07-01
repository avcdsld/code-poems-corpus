def string_to_timestamp(timestring):
    """
    Accepts a str, returns an int timestamp.
    """

    ts = None

    # Uses an extended version of Go's duration string.
    try:
        delta = durationpy.from_str(timestring);
        past = datetime.datetime.utcnow() - delta
        ts = calendar.timegm(past.timetuple())
        return ts
    except Exception as e:
        pass

    if ts:
        return ts
    # else:
    #     print("Unable to parse timestring.")
    return 0