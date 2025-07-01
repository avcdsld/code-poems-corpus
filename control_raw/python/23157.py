def _get_cron_date_time(**kwargs):
    '''
    Returns a dict of date/time values to be used in a cron entry
    '''
    # Define ranges (except daymonth, as it depends on the month)
    range_max = {
        'minute': list(list(range(60))),
        'hour': list(list(range(24))),
        'month': list(list(range(1, 13))),
        'dayweek': list(list(range(7)))
    }

    ret = {}
    for param in ('minute', 'hour', 'month', 'dayweek'):
        value = six.text_type(kwargs.get(param, '1')).lower()
        if value == 'random':
            ret[param] = six.text_type(random.sample(range_max[param], 1)[0])
        elif len(value.split(':')) == 2:
            cron_range = sorted(value.split(':'))
            start, end = int(cron_range[0]), int(cron_range[1])
            ret[param] = six.text_type(random.randint(start, end))
        else:
            ret[param] = value

    if ret['month'] in '1 3 5 7 8 10 12'.split():
        daymonth_max = 31
    elif ret['month'] in '4 6 9 11'.split():
        daymonth_max = 30
    else:
        # This catches both '2' and '*'
        daymonth_max = 28

    daymonth = six.text_type(kwargs.get('daymonth', '1')).lower()
    if daymonth == 'random':
        ret['daymonth'] = \
            six.text_type(random.sample(list(list(range(1, (daymonth_max + 1)))), 1)[0])
    else:
        ret['daymonth'] = daymonth

    return ret