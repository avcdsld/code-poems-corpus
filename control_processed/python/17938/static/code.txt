def get_page(pno, zoom = False, max_size = None, first = False):
    """Return a PNG image for a document page number.
    """
    dlist = dlist_tab[pno]   # get display list of page number
    if not dlist:            # create if not yet there
        dlist_tab[pno] = doc[pno].getDisplayList()
        dlist = dlist_tab[pno]
    r = dlist.rect           # the page rectangle
    clip = r
    # ensure image fits screen:
    # exploit, but do not exceed width or height
    zoom_0 = 1
    if max_size:
        zoom_0 = min(1, max_size[0] / r.width, max_size[1] / r.height)
        if zoom_0 == 1:
            zoom_0 = min(max_size[0] / r.width, max_size[1] / r.height)
    mat_0 = fitz.Matrix(zoom_0, zoom_0)

    if not zoom:             # show total page
        pix = dlist.getPixmap(matrix = mat_0, alpha=False)
    else:
        mp = r.tl + (r.br - r.tl) * 0.5     # page rect center
        w2 = r.width / 2
        h2 = r.height / 2
        clip = r * 0.5
        tl = zoom[0]          # old top-left
        tl.x += zoom[1] * (w2 / 2)
        tl.x = max(0, tl.x)
        tl.x = min(w2, tl.x)
        tl.y += zoom[2] * (h2 / 2)
        tl.y = max(0, tl.y)
        tl.y = min(h2, tl.y)
        clip = fitz.Rect(tl, tl.x + w2, tl.y + h2)

        mat = mat_0 * fitz.Matrix(2, 2)      # zoom matrix
        pix = dlist.getPixmap(alpha=False, matrix=mat, clip=clip)

    if first:                     # first call: tkinter still inactive
        img = pix.getPNGData()    # so use fitz png output
    else:                         # else take tk photo image
        pilimg = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
        img = ImageTk.PhotoImage(pilimg)

    return img, clip.tl