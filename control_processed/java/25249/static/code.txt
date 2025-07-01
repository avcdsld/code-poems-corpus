public static Vec remapDomain(final String[] newDomainValues, final Vec originalVec) throws UnsupportedOperationException, IllegalArgumentException {
    // Sanity checks
    Objects.requireNonNull(newDomainValues);
    if (originalVec.domain() == null)
      throw new UnsupportedOperationException("Unable to remap domain values on a non-categorical vector.");
    if (newDomainValues.length != originalVec.domain().length) {
      throw new IllegalArgumentException(String.format("For each of original domain levels, there must be a new mapping." +
              "There are %o domain levels, however %o mappings were supplied.", originalVec.domain().length, newDomainValues.length));
    }

    // Create a map of new domain values pointing to indices in the array of old domain values in this vec
    final Map<String, Set<Integer>> map = new HashMap<>();
    for (int i = 0; i < newDomainValues.length; i++) {
      Set<Integer> indices = map.get(newDomainValues[i]);
      if (indices == null) {
        indices = new HashSet<>(1);
        indices.add(i);
        map.put(newDomainValues[i], indices);
      } else {
        indices.add(i);
      }
    }

    // Map from the old domain to the new domain
    // There might actually be less domain levels after the transformation
    final int[] indicesMap = MemoryManager.malloc4(originalVec.domain().length);
    final String[] reducedDomain = new String[map.size()];
    int reducedDomainIdx = 0;
    for (String e : map.keySet()) {
      final Set<Integer> oldDomainIndices = map.get(e);
      reducedDomain[reducedDomainIdx] = e;
      for (int idx : oldDomainIndices) {
        indicesMap[idx] = reducedDomainIdx;
      }
      reducedDomainIdx++;
    }

    final RemapDomainTask remapDomainTask = new RemapDomainTask(indicesMap)
            .doAll(new byte[]{Vec.T_CAT}, originalVec);

    // Out of the mist of the RemapDomainTask comes a vector with remapped domain values
    assert remapDomainTask.outputFrame().numCols() == 1;
    Vec remappedVec = remapDomainTask.outputFrame().vec(0);
    remappedVec.setDomain(reducedDomain);

    return remappedVec;
  }