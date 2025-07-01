function rightXorMut(data, padding) {
  const offset = data.length - blockLength;
  for (let i = 0; i < blockLength; i++) {
    data[i + offset] ^= padding[i];
  }
  return data;
}