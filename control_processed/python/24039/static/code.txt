def _split_rules(rules):
    '''
    Split rules with lists into individual rules.

    We accept some attributes as lists or strings. The data we get back from
    the execution module lists rules as individual rules. We need to split the
    provided rules into individual rules to compare them.
    '''
    split = []
    for rule in rules:
        cidr_ip = rule.get('cidr_ip')
        group_name = rule.get('source_group_name')
        group_id = rule.get('source_group_group_id')
        if cidr_ip and not isinstance(cidr_ip, six.string_types):
            for ip in cidr_ip:
                _rule = rule.copy()
                _rule['cidr_ip'] = ip
                split.append(_rule)
        elif group_name and not isinstance(group_name, six.string_types):
            for name in group_name:
                _rule = rule.copy()
                _rule['source_group_name'] = name
                split.append(_rule)
        elif group_id and not isinstance(group_id, six.string_types):
            for _id in group_id:
                _rule = rule.copy()
                _rule['source_group_group_id'] = _id
                split.append(_rule)
        else:
            split.append(rule)
    return split