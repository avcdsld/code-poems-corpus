function combine(a) {
  const fn = function(n, src, got, all) {
    if (n === 0) {
      all.push(got);
      return;
    }

    for (let j = 0; j < src.length; j++) {
      fn(n - 1, src.slice(j + 1), got.concat([src[j]]), all);
    }
  };

  const all = [a];

  for (let i = 0; i < a.length; i++) {
    fn(i, a, [], all);
  }

  all.splice(1, 1); // Remove the empty array

  return all;
}