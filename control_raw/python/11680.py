def get_unit(self, ureg, unit_variations):
        """
        Get the first match unit metric object supported by pint library
        given a variation of unit metric names (Ex:['HOUR', 'hour']).

        :param ureg: unit registry which units are defined and handled
        :type ureg: pint.registry.UnitRegistry object

        :param unit_variations: A list of strings with names of units
        :type unit_variations: str
        """
        for unit in unit_variations:
            try:
                return getattr(ureg, unit)
            except Exception:
                continue
        return None