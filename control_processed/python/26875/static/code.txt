def _strip_dirty(xmltree):
    '''
    Removes dirtyID tags from the candidate config result. Palo Alto devices will make the candidate configuration with
    a dirty ID after a change. This can cause unexpected results when parsing.
    '''
    dirty = xmltree.attrib.pop('dirtyId', None)
    if dirty:
        xmltree.attrib.pop('admin', None)
        xmltree.attrib.pop('time', None)

    for child in xmltree:
        child = _strip_dirty(child)

    return xmltree