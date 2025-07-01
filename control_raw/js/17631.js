function predict(face) {
      const inputDescriptor = getNet().computeFaceDescriptor(face)
      return getDescriptorsByClass().map(ds => ({
        className: ds.className,
        distance: computeMeanDistance(ds.faceDescriptors, inputDescriptor)
      }))
    }