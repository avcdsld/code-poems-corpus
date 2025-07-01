def is_kde_desktop():
    """Detect if we are running in a KDE desktop"""
    if sys.platform.startswith('linux'):
        xdg_desktop = os.environ.get('XDG_CURRENT_DESKTOP', '')
        if xdg_desktop:
            if 'KDE' in xdg_desktop:
                return True
            else:
                return False
        else:
            return False
    else:
        return False