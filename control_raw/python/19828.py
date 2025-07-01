def text(self, max_lines=sys.maxsize):
        """
        Get the scope text, with a possible maximum number of lines.

        :param max_lines: limit the number of lines returned to a maximum.
        :return: str
        """
        ret_val = []
        block = self._trigger.next()
        _, end = self.get_range()
        while (block.isValid() and block.blockNumber() <= end and
               len(ret_val) < max_lines):
            ret_val.append(block.text())
            block = block.next()
        return '\n'.join(ret_val)