def make_dropdown_widget(cls, description='Description', options=['Label 1', 'Label 2'], value='Label 1',
                            file_path=None, layout=Layout(), handler=None):
        "Return a Dropdown widget with specified `handler`."
        dd = widgets.Dropdown(description=description, options=options, value=value, layout=layout)
        if file_path is not None: dd.file_path = file_path
        if handler is not None: dd.observe(handler, names=['value'])
        return dd