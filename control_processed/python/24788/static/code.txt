def edit_config(name, xpath=None, value=None, commit=False):
    '''
    Edits a Palo Alto XPATH to a specific value. This will always overwrite the existing value, even if it is not
    changed.

    You can replace an existing object hierarchy at a specified location in the configuration with a new value. Use
    the xpath parameter to specify the location of the object, including the node to be replaced.

    This is the recommended state to enforce configurations on a xpath.

    name: The name of the module function to execute.

    xpath(str): The XPATH of the configuration API tree to control.

    value(str): The XML value to edit. This must be a child to the XPATH.

    commit(bool): If true the firewall will commit the changes, if false do not commit changes.

    SLS Example:

    .. code-block:: yaml

        panos/addressgroup:
            panos.edit_config:
              - xpath: /config/devices/entry/vsys/entry[@name='vsys1']/address-group/entry[@name='test']
              - value: <static><entry name='test'><member>abc</member><member>xyz</member></entry></static>
              - commit: True

    '''
    ret = _default_ret(name)

    # Verify if the current XPATH is equal to the specified value.
    # If we are equal, no changes required.
    xpath_split = xpath.split("/")

    # Retrieve the head of the xpath for validation.
    if xpath_split:
        head = xpath_split[-1]
        if "[" in head:
            head = head.split("[")[0]

    current_element = __salt__['panos.get_xpath'](xpath)['result']

    if head and current_element and head in current_element:
        current_element = current_element[head]
    else:
        current_element = {}

    new_element = xml.to_dict(ET.fromstring(value), True)

    if current_element == new_element:
        ret.update({
            'comment': 'XPATH is already equal to the specified value.',
            'result': True
        })
        return ret

    result, msg = _edit_config(xpath, value)

    ret.update({
        'comment': msg,
        'result': result
    })

    if not result:
        return ret

    if commit is True:
        ret.update({
            'changes': {'before': current_element, 'after': new_element},
            'commit': __salt__['panos.commit'](),
            'result': True
        })
    else:
        ret.update({
            'changes': {'before': current_element, 'after': new_element},
            'result': True
        })

    return ret