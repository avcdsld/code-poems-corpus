public long finalize64() {
    permuteAndUpdate();
    permuteAndUpdate();
    permuteAndUpdate();
    permuteAndUpdate();
    done = true;
    return v0[0] + v1[0] + mul0[0] + mul1[0];
  }