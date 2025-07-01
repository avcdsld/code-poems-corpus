def get_install_value(self, value_name, wanted_type=None):
        '''
        For the uninstall section of the registry return the name value.

        Args:
            value_name (str): Registry value name.
            wanted_type (str):
                The type of value wanted if the type does not match
                None is return. wanted_type support values are
                ``str`` ``int`` ``list`` ``bytes``.

        Returns:
            value: Value requested or None if not found.
        '''
        try:
            item_value, item_type = self.__reg_query_value(self.__reg_uninstall_handle, value_name)
        except pywintypes.error as exc:  # pylint: disable=no-member
            if exc.winerror == winerror.ERROR_FILE_NOT_FOUND:
                # Not Found
                return None
            raise

        if wanted_type and item_type not in self.__reg_types[wanted_type]:
            item_value = None

        return item_value