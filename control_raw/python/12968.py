def multihead_attention(queries,
                        keys,
                        scope="multihead_attention",
                        num_units=None,
                        num_heads=4,
                        dropout_rate=0,
                        is_training=True,
                        causality=False):
    '''Applies multihead attention.

    Args:
      queries: A 3d tensor with shape of [N, T_q, C_q].
      keys: A 3d tensor with shape of [N, T_k, C_k].
      num_units: A cdscalar. Attention size.
      dropout_rate: A floating point number.
      is_training: Boolean. Controller of mechanism for dropout.
      causality: Boolean. If true, units that reference the future are masked.
      num_heads: An int. Number of heads.
      scope: Optional scope for `variable_scope`.
      reuse: Boolean, whether to reuse the weights of a previous layer
        by the same name.

    Returns
      A 3d tensor with shape of (N, T_q, C)
    '''
    global look5
    with tf.variable_scope(scope):
        # Set the fall back option for num_units
        if num_units is None:
            num_units = queries.get_shape().as_list()[-1]

        Q_ = []
        K_ = []
        V_ = []
        for head_i in range(num_heads):
            Q = tf.layers.dense(queries, num_units / num_heads,
                                activation=tf.nn.relu, name='Query' + str(head_i))  # (N, T_q, C)
            K = tf.layers.dense(keys, num_units / num_heads,
                                activation=tf.nn.relu, name='Key' + str(head_i))  # (N, T_k, C)
            V = tf.layers.dense(keys, num_units / num_heads,
                                activation=tf.nn.relu, name='Value' + str(head_i))  # (N, T_k, C)
            Q_.append(Q)
            K_.append(K)
            V_.append(V)

        # Split and concat
        Q_ = tf.concat(Q_, axis=0)  # (h*N, T_q, C/h)
        K_ = tf.concat(K_, axis=0)  # (h*N, T_k, C/h)
        V_ = tf.concat(V_, axis=0)  # (h*N, T_k, C/h)

        # Multiplication
        outputs = tf.matmul(Q_, tf.transpose(K_, [0, 2, 1]))  # (h*N, T_q, T_k)

        # Scale
        outputs = outputs / (K_.get_shape().as_list()[-1] ** 0.5)

        # Key Masking
        key_masks = tf.sign(tf.abs(tf.reduce_sum(keys, axis=-1)))  # (N, T_k)
        key_masks = tf.tile(key_masks, [num_heads, 1])  # (h*N, T_k)
        key_masks = tf.tile(tf.expand_dims(key_masks, 1),
                            [1, tf.shape(queries)[1], 1])  # (h*N, T_q, T_k)

        paddings = tf.ones_like(outputs) * (-2 ** 32 + 1)
        outputs = tf.where(tf.equal(key_masks, 0), paddings,
                           outputs)  # (h*N, T_q, T_k)

        # Causality = Future blinding
        if causality:
            diag_vals = tf.ones_like(outputs[0, :, :])  # (T_q, T_k)
            tril = tf.contrib.linalg.LinearOperatorTriL(
                diag_vals).to_dense()  # (T_q, T_k)
            masks = tf.tile(tf.expand_dims(tril, 0),
                            [tf.shape(outputs)[0], 1, 1])  # (h*N, T_q, T_k)

            paddings = tf.ones_like(masks) * (-2 ** 32 + 1)
            outputs = tf.where(tf.equal(masks, 0), paddings,
                               outputs)  # (h*N, T_q, T_k)

        # Activation
        look5 = outputs
        outputs = tf.nn.softmax(outputs)  # (h*N, T_q, T_k)

        # Query Masking
        query_masks = tf.sign(
            tf.abs(tf.reduce_sum(queries, axis=-1)))  # (N, T_q)
        query_masks = tf.tile(query_masks, [num_heads, 1])  # (h*N, T_q)
        query_masks = tf.tile(tf.expand_dims(
            query_masks, -1), [1, 1, tf.shape(keys)[1]])  # (h*N, T_q, T_k)
        outputs *= query_masks  # broadcasting. (N, T_q, C)

        # Dropouts
        outputs = dropout(outputs, dropout_rate, is_training)

        # Weighted sum
        outputs = tf.matmul(outputs, V_)  # ( h*N, T_q, C/h)

        # Restore shape
        outputs = tf.concat(tf.split(outputs, num_heads,
                                     axis=0), axis=2)  # (N, T_q, C)

        # Residual connection
        if queries.get_shape().as_list()[-1] == num_units:
            outputs += queries

        # Normalize
        outputs = normalize(outputs, scope=scope)  # (N, T_q, C)

    return outputs