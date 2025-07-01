def PopupGetFolder(message, title=None, default_path='', no_window=False, size=(None, None), button_color=None,
                   background_color=None, text_color=None, icon=DEFAULT_WINDOW_ICON, font=None, no_titlebar=False,
                   grab_anywhere=False, keep_on_top=False, location=(None, None), initial_folder=None):
    """
    Display popup with text entry field and browse button. Browse for folder
    :param message:
    :param default_path:
    :param no_window:
    :param size:
    :param button_color:
    :param background_color:
    :param text_color:
    :param icon:
    :param font:
    :param no_titlebar:
    :param grab_anywhere:
    :param keep_on_top:
    :param location:
    :return: Contents of text field. None if closed using X or cancelled
    """


    if no_window:
        app = wx.App(False)
        frame = wx.Frame()

        if initial_folder:
            dialog = wx.DirDialog(frame, style=wx.FD_OPEN)
        else:
            dialog = wx.DirDialog(frame)
        folder_name = ''
        if dialog.ShowModal() == wx.ID_OK:
            folder_name = dialog.GetPath()
        return folder_name



    layout = [[Text(message, auto_size_text=True, text_color=text_color, background_color=background_color)],
              [InputText(default_text=default_path, size=size), FolderBrowse(initial_folder=initial_folder)],
              [Button('Ok', size=(60, 20), bind_return_key=True), Button('Cancel', size=(60, 20))]]

    _title = title if title is not None else message
    window = Window(title=_title, icon=icon, auto_size_text=True, button_color=button_color,
                    background_color=background_color,
                    font=font, no_titlebar=no_titlebar, grab_anywhere=grab_anywhere, keep_on_top=keep_on_top,
                    location=location)

    (button, input_values) = window.Layout(layout).Read()
    window.Close()
    if button != 'Ok':
        return None
    else:
        path = input_values[0]
        return path