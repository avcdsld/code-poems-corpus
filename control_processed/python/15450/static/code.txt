def project(original_image, perturbed_images, alphas, shape, constraint):
  """ Projection onto given l2 / linf balls in a batch. """
  alphas_shape = [len(alphas)] + [1] * len(shape)
  alphas = alphas.reshape(alphas_shape)
  if constraint == 'l2':
    projected = (1-alphas) * original_image + alphas * perturbed_images
  elif constraint == 'linf':
    projected = clip_image(
        perturbed_images,
        original_image - alphas,
        original_image + alphas
    )
  return projected