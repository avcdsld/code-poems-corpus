def _prefix_from_ip_string(self, ip_str):
        """Turn a netmask/hostmask string into a prefix length

        Args:
            ip_str: The netmask/hostmask to be converted

        Returns:
            An integer, the prefix length.

        Raises:
            NetmaskValueError: If the input is not a valid netmask/hostmask
        """
        # Parse the netmask/hostmask like an IP address.
        try:
            ip_int = self._ip_int_from_string(ip_str)
        except AddressValueError:
            self._report_invalid_netmask(ip_str)

        # Try matching a netmask (this would be /1*0*/ as a bitwise regexp).
        # Note that the two ambiguous cases (all-ones and all-zeroes) are
        # treated as netmasks.
        try:
            return self._prefix_from_ip_int(ip_int)
        except ValueError:
            pass

        # Invert the bits, and try matching a /0+1+/ hostmask instead.
        ip_int ^= self._ALL_ONES
        try:
            return self._prefix_from_ip_int(ip_int)
        except ValueError:
            self._report_invalid_netmask(ip_str)