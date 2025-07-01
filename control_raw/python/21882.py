def add_boolean(self, b):
        """
        Add a boolean value to the stream.

        :param bool b: boolean value to add
        """
        if b:
            self.packet.write(one_byte)
        else:
            self.packet.write(zero_byte)
        return self