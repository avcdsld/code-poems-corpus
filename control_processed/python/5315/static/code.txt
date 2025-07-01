def _idx_to_bits(self, i):
    """Convert an group index to its bit representation."""
    bits = bin(i)[2:].zfill(self.nb_hyperplanes)  # Pad the bits str with 0
    return [-1.0 if b == "0" else 1.0 for b in bits]