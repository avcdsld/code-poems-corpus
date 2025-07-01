def EndVector(self, vectorNumElems):
        """EndVector writes data necessary to finish vector construction."""

        self.assertNested()
        ## @cond FLATBUFFERS_INTERNAL
        self.nested = False
        ## @endcond
        # we already made space for this, so write without PrependUint32
        self.PlaceUOffsetT(vectorNumElems)
        return self.Offset()