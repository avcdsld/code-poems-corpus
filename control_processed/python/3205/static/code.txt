def move(self, xcoord, ycoord):
        """
        Move held tap to specified location.

        :Args:
         - xcoord: X Coordinate to move.
         - ycoord: Y Coordinate to move.
        """
        self._actions.append(lambda: self._driver.execute(
            Command.TOUCH_MOVE, {
                'x': int(xcoord),
                'y': int(ycoord)}))
        return self