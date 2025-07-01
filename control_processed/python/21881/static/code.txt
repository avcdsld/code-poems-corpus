def get_bytes(self, n):
        """
        Return the next ``n`` bytes of the message (as a `str`), without
        decomposing into an int, decoded string, etc.  Just the raw bytes are
        returned. Returns a string of ``n`` zero bytes if there weren't ``n``
        bytes remaining in the message.
        """
        b = self.packet.read(n)
        max_pad_size = 1 << 20  # Limit padding to 1 MB
        if len(b) < n < max_pad_size:
            return b + zero_byte * (n - len(b))
        return b