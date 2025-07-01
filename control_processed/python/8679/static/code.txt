def CreateString(self, s, encoding='utf-8', errors='strict'):
        """CreateString writes a null-terminated byte string as a vector."""

        self.assertNotNested()
        ## @cond FLATBUFFERS_INTERNAL
        self.nested = True
        ## @endcond

        if isinstance(s, compat.string_types):
            x = s.encode(encoding, errors)
        elif isinstance(s, compat.binary_types):
            x = s
        else:
            raise TypeError("non-string passed to CreateString")

        self.Prep(N.UOffsetTFlags.bytewidth, (len(x)+1)*N.Uint8Flags.bytewidth)
        self.Place(0, N.Uint8Flags)

        l = UOffsetTFlags.py_type(len(s))
        ## @cond FLATBUFFERS_INTERNAL
        self.head = UOffsetTFlags.py_type(self.Head() - l)
        ## @endcond
        self.Bytes[self.Head():self.Head()+l] = x

        return self.EndVector(len(x))