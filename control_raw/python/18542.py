def widgetbox(*args, **kwargs):
    """ Create a column of bokeh widgets with predefined styling.

    Args:
        children (list of :class:`~bokeh.models.widgets.widget.Widget`): A list of widgets.

        sizing_mode (``"fixed"``, ``"stretch_both"``, ``"scale_width"``, ``"scale_height"``, ``"scale_both"`` ): How
            will the items in the layout resize to fill the available space.
            Default is ``"fixed"``. For more information on the different
            modes see :attr:`~bokeh.models.layouts.LayoutDOM.sizing_mode`
            description on :class:`~bokeh.models.layouts.LayoutDOM`.

    Returns:
        WidgetBox: A column layout of widget instances all with the same ``sizing_mode``.

    Examples:

        >>> widgetbox([button, select])
        >>> widgetbox(children=[slider], sizing_mode='scale_width')
    """

    sizing_mode = kwargs.pop('sizing_mode', None)
    children = kwargs.pop('children', None)

    children = _handle_children(*args, children=children)

    col_children = []
    for item in children:
        if isinstance(item, LayoutDOM):
            if sizing_mode is not None and _has_auto_sizing(item):
                item.sizing_mode = sizing_mode
            col_children.append(item)
        else:
            raise ValueError("""Only LayoutDOM items can be inserted into a widget box. Tried to insert: %s of type %s""" % (item, type(item)))
    return WidgetBox(children=col_children, sizing_mode=sizing_mode, **kwargs)