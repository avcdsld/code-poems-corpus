def text_list_to_colors_simple(names):
    '''
    Generates a list of colors based on a list of names (strings). Similar strings correspond to similar colors. 
    '''
    uNames = list(set(names))
    uNames.sort()
    textToColor = [ uNames.index(n) for n in names ]
    textToColor = np.array(textToColor)
    textToColor = 255 * (textToColor - textToColor.min()) / \
                  (textToColor.max() - textToColor.min())
    textmaps = generateColorMap();
    colors = [textmaps[int(c)] for c in textToColor]
    return colors