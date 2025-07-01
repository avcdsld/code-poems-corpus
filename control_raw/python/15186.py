def vatm(model,
         x,
         logits,
         eps,
         num_iterations=1,
         xi=1e-6,
         clip_min=None,
         clip_max=None,
         scope=None):
  """
  Tensorflow implementation of the perturbation method used for virtual
  adversarial training: https://arxiv.org/abs/1507.00677
  :param model: the model which returns the network unnormalized logits
  :param x: the input placeholder
  :param logits: the model's unnormalized output tensor (the input to
                 the softmax layer)
  :param eps: the epsilon (input variation parameter)
  :param num_iterations: the number of iterations
  :param xi: the finite difference parameter
  :param clip_min: optional parameter that can be used to set a minimum
                  value for components of the example returned
  :param clip_max: optional parameter that can be used to set a maximum
                  value for components of the example returned
  :param seed: the seed for random generator
  :return: a tensor for the adversarial example
  """
  with tf.name_scope(scope, "virtual_adversarial_perturbation"):
    d = tf.random_normal(tf.shape(x), dtype=tf_dtype)
    for _ in range(num_iterations):
      d = xi * utils_tf.l2_batch_normalize(d)
      logits_d = model.get_logits(x + d)
      kl = utils_tf.kl_with_logits(logits, logits_d)
      Hd = tf.gradients(kl, d)[0]
      d = tf.stop_gradient(Hd)
    d = eps * utils_tf.l2_batch_normalize(d)
    adv_x = x + d
    if (clip_min is not None) and (clip_max is not None):
      adv_x = tf.clip_by_value(adv_x, clip_min, clip_max)
    return adv_x