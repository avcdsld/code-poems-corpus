function linspace (a, b, n) {
  n = n === null ? 100 : n;

  const increment = (b - a) / (n - 1);
  const vector = [];

  while (n-- > 0) {
    vector.push(a);
    a += increment;
  }

  // Make sure the last item will always be "b" because most of the
  // Time we'll get numbers like 1.0000000000000002 instead of 1.
  vector[vector.length - 1] = b;

  return vector;
}