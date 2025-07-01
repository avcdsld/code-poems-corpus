def tf_lanczos_smallest_eigval(vector_prod_fn,
                               matrix_dim,
                               initial_vector,
                               num_iter=1000,
                               max_iter=1000,
                               collapse_tol=1e-9,
                               dtype=tf.float32):
  """Computes smallest eigenvector and eigenvalue using Lanczos in pure TF.

  This function computes smallest eigenvector and eigenvalue of the matrix
  which is implicitly specified by `vector_prod_fn`.
  `vector_prod_fn` is a function which takes `x` and returns a product of matrix
  in consideration and `x`.
  Computation is done using Lanczos algorithm, see
  https://en.wikipedia.org/wiki/Lanczos_algorithm#The_algorithm

  Args:
    vector_prod_fn: function which takes a vector as an input and returns
      matrix vector product.
    matrix_dim: dimentionality of the matrix.
    initial_vector: guess vector to start the algorithm with
    num_iter: user-defined number of iterations for the algorithm
    max_iter: maximum number of iterations.
    collapse_tol: tolerance to determine collapse of the Krylov subspace
    dtype: type of data

  Returns:
    tuple of (eigenvalue, eigenvector) of smallest eigenvalue and corresponding
    eigenvector.
  """

  # alpha will store diagonal elements
  alpha = tf.TensorArray(dtype, size=1, dynamic_size=True, element_shape=())
  # beta will store off diagonal elements
  beta = tf.TensorArray(dtype, size=0, dynamic_size=True, element_shape=())
  # q will store Krylov space basis
  q_vectors = tf.TensorArray(
      dtype, size=1, dynamic_size=True, element_shape=(matrix_dim, 1))

  # If start vector is all zeros, make it a random normal vector and run for max_iter
  if tf.norm(initial_vector) < collapse_tol:
    initial_vector = tf.random_normal(shape=(matrix_dim, 1), dtype=dtype)
    num_iter = max_iter

  w = initial_vector / tf.norm(initial_vector)

  # Iteration 0 of Lanczos
  q_vectors = q_vectors.write(0, w)
  w_ = vector_prod_fn(w)
  cur_alpha = tf.reduce_sum(w_ * w)
  alpha = alpha.write(0, cur_alpha)
  w_ = w_ - tf.scalar_mul(cur_alpha, w)
  w_prev = w
  w = w_

  # Subsequent iterations of Lanczos
  for i in tf.range(1, num_iter):
    cur_beta = tf.norm(w)
    if cur_beta < collapse_tol:
      # return early if Krylov subspace collapsed
      break

    # cur_beta is larger than collapse_tol,
    # so division will return finite result.
    w = w / cur_beta

    w_ = vector_prod_fn(w)
    cur_alpha = tf.reduce_sum(w_ * w)

    q_vectors = q_vectors.write(i, w)
    alpha = alpha.write(i, cur_alpha)
    beta = beta.write(i-1, cur_beta)

    w_ = w_ - tf.scalar_mul(cur_alpha, w) - tf.scalar_mul(cur_beta, w_prev)
    w_prev = w
    w = w_

  alpha = alpha.stack()
  beta = beta.stack()
  q_vectors = tf.reshape(q_vectors.stack(), (-1, matrix_dim))

  offdiag_submatrix = tf.linalg.diag(beta)
  tridiag_matrix = (tf.linalg.diag(alpha)
                    + tf.pad(offdiag_submatrix, [[0, 1], [1, 0]])
                    + tf.pad(offdiag_submatrix, [[1, 0], [0, 1]]))

  eigvals, eigvecs = tf.linalg.eigh(tridiag_matrix)

  smallest_eigval = eigvals[0]
  smallest_eigvec = tf.matmul(tf.reshape(eigvecs[:, 0], (1, -1)),
                              q_vectors)
  smallest_eigvec = smallest_eigvec / tf.norm(smallest_eigvec)
  smallest_eigvec = tf.reshape(smallest_eigvec, (matrix_dim, 1))

  return smallest_eigval, smallest_eigvec