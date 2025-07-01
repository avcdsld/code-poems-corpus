def dedup(l, suffix='__', case_sensitive=True):
    """De-duplicates a list of string by suffixing a counter

    Always returns the same number of entries as provided, and always returns
    unique values. Case sensitive comparison by default.

    >>> print(','.join(dedup(['foo', 'bar', 'bar', 'bar', 'Bar'])))
    foo,bar,bar__1,bar__2,Bar
    >>> print(','.join(dedup(['foo', 'bar', 'bar', 'bar', 'Bar'], case_sensitive=False)))
    foo,bar,bar__1,bar__2,Bar__3
    """
    new_l = []
    seen = {}
    for s in l:
        s_fixed_case = s if case_sensitive else s.lower()
        if s_fixed_case in seen:
            seen[s_fixed_case] += 1
            s += suffix + str(seen[s_fixed_case])
        else:
            seen[s_fixed_case] = 0
        new_l.append(s)
    return new_l