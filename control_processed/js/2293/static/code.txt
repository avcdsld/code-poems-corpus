function hasProblematicOverloading(instances) {
    // Check if there are same lengthed argument sets
    const knownLengths = [];
    return instances.map(({ args }) => args.length).reduce((carry, item) => {
      if (carry || knownLengths.some((l) => l === item)) {
        return true;
      }

      knownLengths.push(item);
      return false;
    }, false);
  }