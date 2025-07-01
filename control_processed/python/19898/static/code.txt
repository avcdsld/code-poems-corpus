def save_bookmarks(filename, bookmarks):
    """Save all bookmarks from specific file to config."""
    if not osp.isfile(filename):
        return
    slots = load_bookmarks_without_file(filename)
    for slot_num, content in bookmarks.items():
        slots[slot_num] = [filename, content[0], content[1]]
    CONF.set('editor', 'bookmarks', slots)