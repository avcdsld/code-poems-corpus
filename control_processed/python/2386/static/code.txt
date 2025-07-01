def _convert_to_border(cls, border_dict):
        """
        Convert ``border_dict`` to an openpyxl v2 Border object
        Parameters
        ----------
        border_dict : dict
            A dict with zero or more of the following keys (or their synonyms).
                'left'
                'right'
                'top'
                'bottom'
                'diagonal'
                'diagonal_direction'
                'vertical'
                'horizontal'
                'diagonalUp' ('diagonalup')
                'diagonalDown' ('diagonaldown')
                'outline'
        Returns
        -------
        border : openpyxl.styles.Border
        """

        from openpyxl.styles import Border

        _border_key_map = {
            'diagonalup': 'diagonalUp',
            'diagonaldown': 'diagonalDown',
        }

        border_kwargs = {}
        for k, v in border_dict.items():
            if k in _border_key_map:
                k = _border_key_map[k]
            if k == 'color':
                v = cls._convert_to_color(v)
            if k in ['left', 'right', 'top', 'bottom', 'diagonal']:
                v = cls._convert_to_side(v)
            border_kwargs[k] = v

        return Border(**border_kwargs)