def first(self, rows: List[Row]) -> List[Row]:
        """
        Takes an expression that evaluates to a list of rows, and returns the first one in that
        list.
        """
        if not rows:
            logger.warning("Trying to get first row from an empty list")
            return []
        return [rows[0]]