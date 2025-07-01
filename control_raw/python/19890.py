def is_dark_font_color(color_scheme):
    """Check if the font color used in the color scheme is dark."""
    color_scheme = get_color_scheme(color_scheme)
    font_color, fon_fw, fon_fs = color_scheme['normal']
    return dark_color(font_color)