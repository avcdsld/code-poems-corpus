def upgrade_code(self):
        '''
        For installers which follow the Microsoft Installer standard, returns
        the ``Upgrade code``.

        Returns:
            value (str): ``Upgrade code`` GUID for installed software.
        '''
        if not self.__squid:
            # Must have a valid squid for an upgrade code to exist
            return ''

        # GUID/SQUID are unique, so it does not matter if they are 32bit or
        # 64bit or user install so all items are cached into a single dict
        have_scan_key = '{0}\\{1}\\{2}'.format(self.__reg_hive, self.__reg_upgradecode_path, self.__reg_32bit)
        if not self.__upgrade_codes or self.__reg_key_guid not in self.__upgrade_codes:
            # Read in the upgrade codes in this section of the registry.
            try:
                uc_handle = win32api.RegOpenKeyEx(getattr(win32con, self.__reg_hive),  # pylint: disable=no-member
                                                  self.__reg_upgradecode_path,
                                                  0,
                                                  win32con.KEY_READ | self.__reg_32bit_access)
            except pywintypes.error as exc:  # pylint: disable=no-member
                if exc.winerror == winerror.ERROR_FILE_NOT_FOUND:
                    # Not Found
                    log.warning(
                        'Not Found %s\\%s 32bit %s',
                        self.__reg_hive,
                        self.__reg_upgradecode_path,
                        self.__reg_32bit
                    )
                    return ''
                raise
            squid_upgrade_code_all, _, _, suc_pytime = zip(*win32api.RegEnumKeyEx(uc_handle))  # pylint: disable=no-member

            # Check if we have already scanned these upgrade codes before, and also
            # check if they have been updated in the registry since last time we scanned.
            if (have_scan_key in self.__upgrade_code_have_scan and
                    self.__upgrade_code_have_scan[have_scan_key] == (squid_upgrade_code_all, suc_pytime)):
                log.debug('Scan skipped for upgrade codes, no changes (%s)', have_scan_key)
                return ''  # we have scanned this before and no new changes.

            # Go into each squid upgrade code and find all the related product codes.
            log.debug('Scan for upgrade codes (%s) for product codes', have_scan_key)
            for upgrade_code_squid in squid_upgrade_code_all:
                upgrade_code_guid = self.__squid_to_guid(upgrade_code_squid)
                pc_handle = win32api.RegOpenKeyEx(uc_handle,  # pylint: disable=no-member
                                                  upgrade_code_squid,
                                                  0,
                                                  win32con.KEY_READ | self.__reg_32bit_access)
                _, pc_val_count, _ = win32api.RegQueryInfoKey(pc_handle)  # pylint: disable=no-member
                for item_index in range(pc_val_count):
                    product_code_guid = \
                        self.__squid_to_guid(win32api.RegEnumValue(pc_handle, item_index)[0])  # pylint: disable=no-member
                    if product_code_guid:
                        self.__upgrade_codes[product_code_guid] = upgrade_code_guid
                win32api.RegCloseKey(pc_handle)  # pylint: disable=no-member

            win32api.RegCloseKey(uc_handle)  # pylint: disable=no-member
            self.__upgrade_code_have_scan[have_scan_key] = (squid_upgrade_code_all, suc_pytime)

        return self.__upgrade_codes.get(self.__reg_key_guid, '')