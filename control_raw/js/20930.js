function (start) {
    var index = start || 0,
      length = this.string.length,
      region = length;

    while (index < length - 1 && region === length) {
      if (this.hasVowelAtIndex(index) && !this.hasVowelAtIndex(index + 1)) {
        region = index + 2;
      }
      index++;
    }

    return region;
  }