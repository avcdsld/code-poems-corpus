def _get_cell_parts(cls, cell_text: str) -> List[Tuple[str, str]]:
        """
        Splits a cell into parts and returns the parts of the cell.  We return a list of
        ``(entity_name, entity_text)``, where ``entity_name`` is ``fb:part.[something]``, and
        ``entity_text`` is the text of the cell corresponding to that part.  For many cells, there
        is only one "part", and we return a list of length one.

        Note that you shouldn't call this on every cell in the table; SEMPRE decides to make these
        splits only when at least one of the cells in a column looks "splittable".  Only if you're
        splitting the cells in a column should you use this function.
        """
        parts = []
        for part_text in cls.cell_part_regex.split(cell_text):
            part_text = part_text.strip()
            part_entity = f'fb:part.{cls._normalize_string(part_text)}'
            parts.append((part_entity, part_text))
        return parts