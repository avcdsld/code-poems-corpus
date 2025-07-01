function toMatch(ss) {
    return {
      match: ss[0],
      groups: Z.map (B (reject (equals (undefined))) (Just), ss.slice (1))
    };
  }