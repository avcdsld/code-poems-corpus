public void compress3( AutoBuffer ab ) {
    assert max() > 32;         // Expect a larger format
    assert _byteoff == 0;       // This is only set on loading a pre-existing IcedBitSet
    assert _val.length==numBytes();
    ab.put2((char)_bitoff);
    ab.put4(_nbits);
    ab.putA1(_val,_val.length);
  }