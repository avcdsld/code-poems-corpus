def make_m_psd(self, original_nu, feed_dictionary):
    """Run binary search to find a value for nu that makes M PSD
    Args:
      original_nu: starting value of nu to do binary search on
      feed_dictionary: dictionary of updated lambda variables to feed into M
    Returns:
      new_nu: new value of nu
    """
    feed_dict = feed_dictionary.copy()
    _, min_eig_val_m = self.get_lanczos_eig(compute_m=True, feed_dict=feed_dict)

    lower_nu = original_nu
    upper_nu = original_nu
    num_iter = 0

    # Find an upper bound on nu
    while min_eig_val_m - TOL < 0 and num_iter < (MAX_BINARY_SEARCH_ITER / 2):
      num_iter += 1
      upper_nu *= NU_UPDATE_CONSTANT
      feed_dict.update({self.nu: upper_nu})
      _, min_eig_val_m = self.get_lanczos_eig(compute_m=True, feed_dict=feed_dict)

    final_nu = upper_nu

    # Perform binary search to find best value of nu
    while lower_nu <= upper_nu and num_iter < MAX_BINARY_SEARCH_ITER:
      num_iter += 1
      mid_nu = (lower_nu + upper_nu) / 2
      feed_dict.update({self.nu: mid_nu})
      _, min_eig_val_m = self.get_lanczos_eig(compute_m=True, feed_dict=feed_dict)
      if min_eig_val_m - TOL < 0:
        lower_nu = mid_nu
      else:
        upper_nu = mid_nu

    final_nu = upper_nu

    return final_nu