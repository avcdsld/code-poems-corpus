def CreateByteVector(self, x):
        """CreateString writes a byte vector."""

        self.assertNotNested()
        ## @cond FLATBUFFERS_INTERNAL
        self.nested = True
        ## @endcond

        if not isinstance(x, compat.binary_types):
            raise TypeError("non-byte vector passed to CreateByteVector")

        self.Prep(N.UOffsetTFlags.bytewidth, len(x)*N.Uint8Flags.bytewidth)

        l = UOffsetTFlags.py_type(len(x))
        ## @cond FLATBUFFERS_INTERNAL
        self.head = UOffsetTFlags.py_type(self.Head() - l)
        ## @endcond
        self.Bytes[self.Head():self.Head()+l] = x

        return self.EndVector(len(x))