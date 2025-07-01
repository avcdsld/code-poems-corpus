def construct_lanczos_params(self):
    """Computes matrices T and V using the Lanczos algorithm.

    Args:
      k: number of iterations and dimensionality of the tridiagonal matrix
    Returns:
      eig_vec: eigen vector corresponding to min eigenvalue
    """
    # Using autograph to automatically handle
    # the control flow of minimum_eigen_vector
    self.min_eigen_vec = autograph.to_graph(utils.tf_lanczos_smallest_eigval)

    def _m_vector_prod_fn(x):
      return self.get_psd_product(x, dtype=self.lanczos_dtype)
    def _h_vector_prod_fn(x):
      return self.get_h_product(x, dtype=self.lanczos_dtype)

    # Construct nodes for computing eigenvalue of M
    self.m_min_vec_estimate = np.zeros(shape=(self.matrix_m_dimension, 1), dtype=np.float64)
    zeros_m = tf.zeros(shape=(self.matrix_m_dimension, 1), dtype=tf.float64)
    self.m_min_vec_ph = tf.placeholder_with_default(input=zeros_m,
                                                    shape=(self.matrix_m_dimension, 1),
                                                    name='m_min_vec_ph')
    self.m_min_eig, self.m_min_vec = self.min_eigen_vec(_m_vector_prod_fn,
                                                        self.matrix_m_dimension,
                                                        self.m_min_vec_ph,
                                                        self.lzs_params['max_iter'],
                                                        dtype=self.lanczos_dtype)
    self.m_min_eig = tf.cast(self.m_min_eig, self.nn_dtype)
    self.m_min_vec = tf.cast(self.m_min_vec, self.nn_dtype)

    self.h_min_vec_estimate = np.zeros(shape=(self.matrix_m_dimension - 1, 1), dtype=np.float64)
    zeros_h = tf.zeros(shape=(self.matrix_m_dimension - 1, 1), dtype=tf.float64)
    self.h_min_vec_ph = tf.placeholder_with_default(input=zeros_h,
                                                    shape=(self.matrix_m_dimension - 1, 1),
                                                    name='h_min_vec_ph')
    self.h_min_eig, self.h_min_vec = self.min_eigen_vec(_h_vector_prod_fn,
                                                        self.matrix_m_dimension-1,
                                                        self.h_min_vec_ph,
                                                        self.lzs_params['max_iter'],
                                                        dtype=self.lanczos_dtype)
    self.h_min_eig = tf.cast(self.h_min_eig, self.nn_dtype)
    self.h_min_vec = tf.cast(self.h_min_vec, self.nn_dtype)