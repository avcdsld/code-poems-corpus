function calculateCollatzConjecture(number) {
  if (!(number in cache)) {
    if (number % 2 === 0) cache[number] = number >> 1;
    else cache[number] = number * 3 + 1;
  }

  return cache[number];
}