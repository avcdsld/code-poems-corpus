def install_time(self):
        '''
        Return the install time, or provide an estimate of install time.

        Installers or even self upgrading software must/should update the date
        held within InstallDate field when they change versions. Some installers
        do not set ``InstallDate`` at all so we use the last modified time on the
        registry key.

        Returns:
            int: Seconds since 1970 UTC.
        '''
        time1970 = self.__mod_time1970  # time of last resort
        try:
            # pylint: disable=no-member
            date_string, item_type = \
                win32api.RegQueryValueEx(self.__reg_uninstall_handle, 'InstallDate')
        except pywintypes.error as exc:  # pylint: disable=no-member
            if exc.winerror == winerror.ERROR_FILE_NOT_FOUND:
                return time1970  # i.e. use time of last resort
            else:
                raise

        if item_type == win32con.REG_SZ:
            try:
                date_object = datetime.datetime.strptime(date_string, "%Y%m%d")
                time1970 = time.mktime(date_object.timetuple())
            except ValueError:  # date format is not correct
                pass

        return time1970