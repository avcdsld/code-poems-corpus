def regxy(pattern, response, supress_regex, custom):
    """Extract a string based on regex pattern supplied by user."""
    try:
        matches = re.findall(r'%s' % pattern, response)
        for match in matches:
            verb('Custom regex', match)
            custom.add(match)
    except:
        supress_regex = True