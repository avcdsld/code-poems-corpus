def _render_tab(lst):
    '''
    Takes a tab list structure and renders it to a list for applying it to
    a file
    '''
    ret = []
    for pre in lst['pre']:
        ret.append('{0}\n'.format(pre))
    if ret:
        if ret[-1] != TAG:
            ret.append(TAG)
    else:
        ret.append(TAG)
    for env in lst['env']:
        if (env['value'] is None) or (env['value'] == ""):
            ret.append('{0}=""\n'.format(env['name']))
        else:
            ret.append('{0}={1}\n'.format(env['name'], env['value']))
    for cron in lst['crons']:
        if cron['comment'] is not None or cron['identifier'] is not None:
            comment = '#'
            if cron['comment']:
                comment += ' {0}'.format(
                    cron['comment'].replace('\n', '\n# '))
            if cron['identifier']:
                comment += ' {0}:{1}'.format(SALT_CRON_IDENTIFIER,
                                             cron['identifier'])

            comment += '\n'
            ret.append(comment)
        ret.append('{0}{1} {2} {3} {4} {5} {6}\n'.format(
                            cron['commented'] is True and '#DISABLED#' or '',
                            cron['minute'],
                            cron['hour'],
                            cron['daymonth'],
                            cron['month'],
                            cron['dayweek'],
                            cron['cmd']
                            )
                   )
    for cron in lst['special']:
        if cron['comment'] is not None or cron['identifier'] is not None:
            comment = '#'
            if cron['comment']:
                comment += ' {0}'.format(
                    cron['comment'].rstrip().replace('\n', '\n# '))
            if cron['identifier']:
                comment += ' {0}:{1}'.format(SALT_CRON_IDENTIFIER,
                                             cron['identifier'])

            comment += '\n'
            ret.append(comment)
        ret.append('{0}{1} {2}\n'.format(
                            cron['commented'] is True and '#DISABLED#' or '',
                            cron['spec'],
                            cron['cmd']
                            )
                  )
    return ret