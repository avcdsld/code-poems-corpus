def enumerate_tiles(tiles):
  """
  Convenience
  """
  enumerated = []
  for key in tiles.keys():
    enumerated.append((key[0], key[1], tiles[key]))
  return enumerated