def sample_view(min_dist, max_dist=None):
  '''Sample random camera position.
  
  Sample origin directed camera position in given distance
  range from the origin. ModelView matrix is returned.
  '''
  if max_dist is None:
    max_dist = min_dist
  dist = np.random.uniform(min_dist, max_dist)
  eye = np.random.normal(size=3)
  eye = normalize(eye)*dist
  return lookat(eye)