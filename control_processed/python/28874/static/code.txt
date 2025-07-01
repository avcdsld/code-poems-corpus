def __reg_query_value(handle, value_name):
        '''
        Calls RegQueryValueEx

        If PY2 ensure unicode string and expand REG_EXPAND_SZ before returning
        Remember to catch not found exceptions when calling.

        Args:
            handle (object): open registry handle.
            value_name (str): Name of the value you wished returned

        Returns:
            tuple: type, value
        '''
        # item_value, item_type = win32api.RegQueryValueEx(self.__reg_uninstall_handle, value_name)
        item_value, item_type = win32api.RegQueryValueEx(handle, value_name)  # pylint: disable=no-member
        if six.PY2 and isinstance(item_value, six.string_types) and not isinstance(item_value, six.text_type):
            try:
                item_value = six.text_type(item_value, encoding='mbcs')
            except UnicodeError:
                pass
        if item_type == win32con.REG_EXPAND_SZ:
            # expects Unicode input
            win32api.ExpandEnvironmentStrings(item_value)  # pylint: disable=no-member
            item_type = win32con.REG_SZ
        return item_value, item_type