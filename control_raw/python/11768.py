def aggregate_tile(cells, ti, tj, aggregate, params, metadata, layout, summary):
  """
    Call the user defined aggregation function on each cell and combine into a single json object
  """
  tile = []
  keys = cells.keys()
  for i,key in enumerate(keys):
    print("cell", i+1, "/", len(keys), end='\r')
    cell_json = aggregate(cells[key], params, metadata, layout, summary)
    tile.append({"aggregate":cell_json, "i":int(key[0]), "j":int(key[1])})
  return tile