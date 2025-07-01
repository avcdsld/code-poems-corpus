def grid_visual(*args, **kwargs):
  """Deprecation wrapper"""
  warnings.warn("`grid_visual` has moved to `cleverhans.plot.pyplot_image`. "
                "cleverhans.utils.grid_visual may be removed on or after "
                "2019-04-24.")
  from cleverhans.plot.pyplot_image import grid_visual as new_grid_visual
  return new_grid_visual(*args, **kwargs)