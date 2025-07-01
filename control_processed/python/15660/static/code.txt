def create(dataset, label=None, features=None, distance=None, method='auto',
           verbose=True, **kwargs):
    """
    Create a nearest neighbor model, which can be searched efficiently and
    quickly for the nearest neighbors of a query observation. If the `method`
    argument is specified as `auto`, the type of model is chosen automatically
    based on the type of data in `dataset`.

    .. warning::

        The 'dot_product' distance is deprecated and will be removed in future
        versions of Turi Create. Please use 'transformed_dot_product'
        distance instead, although note that this is more than a name change;
        it is a *different* transformation of the dot product of two vectors.
        Please see the distances module documentation for more details.

    Parameters
    ----------
    dataset : SFrame
        Reference data. If the features for each observation are numeric, they
        may be in separate columns of 'dataset' or a single column with lists
        of values. The features may also be in the form of a column of sparse
        vectors (i.e. dictionaries), with string keys and numeric values.

    label : string, optional
        Name of the SFrame column with row labels. If 'label' is not specified,
        row numbers are used to identify reference dataset rows when the model
        is queried.

    features : list[string], optional
        Name of the columns with features to use in computing distances between
        observations and the query points. 'None' (the default) indicates that
        all columns except the label should be used as features. Each column
        can be one of the following types:

        - *Numeric*: values of numeric type integer or float.

        - *Array*: list of numeric (integer or float) values. Each list element
          is treated as a separate variable in the model.

        - *Dictionary*: key-value pairs with numeric (integer or float) values.
          Each key indicates a separate variable in the model.

        - *List*: list of integer or string values. Each element is treated as
          a separate variable in the model.

        - *String*: string values.

        Please note: if a composite distance is also specified, this parameter
        is ignored.

    distance : string, function, or list[list], optional
        Function to measure the distance between any two input data rows. This
        may be one of three types:

        - *String*: the name of a standard distance function. One of
          'euclidean', 'squared_euclidean', 'manhattan', 'levenshtein',
          'jaccard', 'weighted_jaccard', 'cosine', 'dot_product' (deprecated),
          or 'transformed_dot_product'.

        - *Function*: a function handle from the
          :mod:`~turicreate.toolkits.distances` module.

        - *Composite distance*: the weighted sum of several standard distance
          functions applied to various features. This is specified as a list of
          distance components, each of which is itself a list containing three
          items:

          1. list or tuple of feature names (strings)

          2. standard distance name (string)

          3. scaling factor (int or float)

        For more information about Turi Create distance functions, please
        see the :py:mod:`~turicreate.toolkits.distances` module.

        If 'distance' is left unspecified or set to 'auto', a composite
        distance is constructed automatically based on feature types.

    method : {'auto', 'ball_tree', 'brute_force', 'lsh'}, optional
        Method for computing nearest neighbors. The options are:

        - *auto* (default): the method is chosen automatically, based on the
          type of data and the distance. If the distance is 'manhattan' or
          'euclidean' and the features are numeric or vectors of numeric
          values, then the 'ball_tree' method is used. Otherwise, the
          'brute_force' method is used.

        - *ball_tree*: use a tree structure to find the k-closest neighbors to
          each query point. The ball tree model is slower to construct than the
          brute force model, but queries are faster than linear time. This
          method is not applicable for the cosine and dot product distances.
          See `Liu, et al (2004)
          <http://papers.nips.cc/paper/2666-an-investigation-of-p
          ractical-approximat e-nearest-neighbor-algorithms>`_ for
          implementation details.

        - *brute_force*: compute the distance from a query point to all
          reference observations. There is no computation time for model
          creation with the brute force method (although the reference data is
          held in the model, but each query takes linear time.

        - *lsh*: use Locality Sensitive Hashing (LSH) to find approximate
          nearest neighbors efficiently. The LSH model supports 'euclidean',
          'squared_euclidean', 'manhattan', 'cosine', 'jaccard', 'dot_product'
          (deprecated), and 'transformed_dot_product' distances. Two options
          are provided for LSH -- ``num_tables`` and
          ``num_projections_per_table``. See the notes below for details.

    verbose: bool, optional
        If True, print progress updates and model details.

    **kwargs : optional
        Options for the distance function and query method.

        - *leaf_size*: for the ball tree method, the number of points in each
          leaf of the tree. The default is to use the max of 1,000 and
          n/(2^11), which ensures a maximum tree depth of 12.

        - *num_tables*: For the LSH method, the number of hash tables
          constructed. The default value is 20. We recommend choosing values
          from 10 to 30.

        - *num_projections_per_table*: For the LSH method, the number of
          projections/hash functions for each hash table. The default value is
          4 for 'jaccard' distance, 16 for 'cosine' distance and 8 for other
          distances. We recommend using number 2 ~ 6 for 'jaccard' distance, 8
          ~ 20 for 'cosine' distance and 4 ~ 12 for other distances.

    Returns
    -------
    out : NearestNeighborsModel
        A structure for efficiently computing the nearest neighbors in 'dataset'
        of new query points.

    See Also
    --------
    NearestNeighborsModel.query, turicreate.toolkits.distances

    Notes
    -----
    - Missing data is not allowed in the 'dataset' provided to this function.
      Please use the :func:`turicreate.SFrame.fillna` and
      :func:`turicreate.SFrame.dropna` utilities to handle missing data before
      creating a nearest neighbors model.

    - Missing keys in sparse vectors are assumed to have value 0.

    - The `composite_params` parameter was removed as of Turi Create
      version 1.5. The `distance` parameter now accepts either standard or
      composite distances. Please see the :mod:`~turicreate.toolkits.distances`
      module documentation for more information on composite distances.

    - If the features should be weighted equally in the distance calculations
      but are measured on different scales, it is important to standardize the
      features. One way to do this is to subtract the mean of each column and
      divide by the standard deviation.

    **Locality Sensitive Hashing (LSH)**

    There are several efficient nearest neighbors search algorithms that work
    well for data with low dimensions :math:`d` (approximately 50). However,
    most of the solutions suffer from either space or query time that is
    exponential in :math:`d`. For large :math:`d`, they often provide little,
    if any, improvement over the 'brute_force' method. This is a well-known
    consequence of the phenomenon called `The Curse of Dimensionality`.

    `Locality Sensitive Hashing (LSH)
    <https://en.wikipedia.org/wiki/Locality-sensitive_hashing>`_ is an approach
    that is designed to efficiently solve the *approximate* nearest neighbor
    search problem for high dimensional data. The key idea of LSH is to hash
    the data points using several hash functions, so that the probability of
    collision is much higher for data points which are close to each other than
    those which are far apart.

    An LSH family is a family of functions :math:`h` which map points from the
    metric space to a bucket, so that

    - if :math:`d(p, q) \\leq R`, then :math:`h(p) = h(q)` with at least probability :math:`p_1`.
    - if :math:`d(p, q) \\geq cR`, then :math:`h(p) = h(q)` with probability at most :math:`p_2`.

    LSH for efficient approximate nearest neighbor search:

    - We define a new family of hash functions :math:`g`, where each
      function :math:`g` is obtained by concatenating :math:`k` functions
      :math:`h_1, ..., h_k`, i.e., :math:`g(p)=[h_1(p),...,h_k(p)]`.
      The algorithm constructs :math:`L` hash tables, each of which
      corresponds to a different randomly chosen hash function :math:`g`.
      There are :math:`k \\cdot L` hash functions used in total.

    - In the preprocessing step, we hash all :math:`n` reference points
      into each of the :math:`L` hash tables.

    - Given a query point :math:`q`, the algorithm iterates over the
      :math:`L` hash functions :math:`g`. For each :math:`g` considered, it
      retrieves the data points that are hashed into the same bucket as q.
      These data points from all the :math:`L` hash tables are considered as
      candidates that are then re-ranked by their real distances with the query
      data.

    **Note** that the number of tables :math:`L` and the number of hash
    functions per table :math:`k` are two main parameters. They can be set
    using the options ``num_tables`` and ``num_projections_per_table``
    respectively.

    Hash functions for different distances:

    - `euclidean` and `squared_euclidean`:
      :math:`h(q) = \\lfloor \\frac{a \\cdot q + b}{w} \\rfloor` where
      :math:`a` is a vector, of which the elements are independently
      sampled from normal distribution, and :math:`b` is a number
      uniformly sampled from :math:`[0, r]`. :math:`r` is a parameter for the
      bucket width. We set :math:`r` using the average all-pair `euclidean`
      distances from a small randomly sampled subset of the reference data.

    - `manhattan`: The hash function of `manhattan` is similar with that of
      `euclidean`. The only difference is that the elements of `a` are sampled
      from Cauchy distribution, instead of normal distribution.

    - `cosine`: Random Projection is designed to approximate the cosine
      distance between vectors. The hash function is :math:`h(q) = sgn(a \\cdot
      q)`, where :math:`a` is randomly sampled normal unit vector.

    - `jaccard`: We use a recently proposed method one permutation hashing by
      Shrivastava and Li. See the paper `[Shrivastava and Li, UAI 2014]
      <http://www.auai.org/uai2014/proceedings/individuals/225.pdf>`_ for
      details.

    - `dot_product`: The reference data points are first transformed to
      fixed-norm vectors, and then the minimum `dot_product` distance search
      problem can be solved via finding the reference data with smallest
      `cosine` distances. See the paper `[Neyshabur and Srebro, ICML 2015]
      <http://proceedings.mlr.press/v37/neyshabur15.html>`_ for details.

    References
    ----------
    - `Wikipedia - nearest neighbor
      search <http://en.wikipedia.org/wiki/Nearest_neighbor_search>`_

    - `Wikipedia - ball tree <http://en.wikipedia.org/wiki/Ball_tree>`_

    - Ball tree implementation: Liu, T., et al. (2004) `An Investigation of
      Practical Approximate Nearest Neighbor Algorithms
      <http://papers.nips.cc/paper/2666-an-investigation-of-p
      ractical-approximat e-nearest-neighbor-algorithms>`_. Advances in Neural
      Information Processing Systems pp. 825-832.

    - `Wikipedia - Jaccard distance
      <http://en.wikipedia.org/wiki/Jaccard_index>`_

    - Weighted Jaccard distance: Chierichetti, F., et al. (2010) `Finding the
      Jaccard Median
      <http://theory.stanford.edu/~sergei/papers/soda10-jaccard.pdf>`_.
      Proceedings of the Twenty-First Annual ACM-SIAM Symposium on Discrete
      Algorithms. Society for Industrial and Applied Mathematics.

    - `Wikipedia - Cosine distance
      <http://en.wikipedia.org/wiki/Cosine_similarity>`_

    - `Wikipedia - Levenshtein distance
      <http://en.wikipedia.org/wiki/Levenshtein_distance>`_

    - Locality Sensitive Hashing : Chapter 3 of the book `Mining Massive
      Datasets <http://infolab.stanford.edu/~ullman/mmds/ch3.pdf>`_.

    Examples
    --------
    Construct a nearest neighbors model with automatically determined method
    and distance:

    >>> sf = turicreate.SFrame({'X1': [0.98, 0.62, 0.11],
    ...                       'X2': [0.69, 0.58, 0.36],
    ...                       'str_feature': ['cat', 'dog', 'fossa']})
    >>> model = turicreate.nearest_neighbors.create(sf, features=['X1', 'X2'])

    For datasets with a large number of rows and up to about 100 variables, the
    ball tree method often leads to much faster queries.

    >>> model = turicreate.nearest_neighbors.create(sf, features=['X1', 'X2'],
    ...                                           method='ball_tree')

    Often the final determination of a neighbor is based on several distance
    computations over different sets of features. Each part of this composite
    distance may have a different relative weight.

    >>> my_dist = [[['X1', 'X2'], 'euclidean', 2.],
    ...            [['str_feature'], 'levenshtein', 3.]]
    ...
    >>> model = turicreate.nearest_neighbors.create(sf, distance=my_dist)
    """

    ## Validate the 'dataset' input
    _tkutl._raise_error_if_not_sframe(dataset, "dataset")
    _tkutl._raise_error_if_sframe_empty(dataset, "dataset")

    ## Basic validation of the features input
    if features is not None and not isinstance(features, list):
        raise TypeError("If specified, input 'features' must be a list of " +
                        "strings.")

    ## Clean the method options and create the options dictionary
    allowed_kwargs = ['leaf_size', 'num_tables', 'num_projections_per_table']
    _method_options = {}

    for k, v in kwargs.items():
        if k in allowed_kwargs:
            _method_options[k] = v
        else:
            raise _ToolkitError("'{}' is not a valid keyword argument".format(k) +
                                " for the nearest neighbors model. Please " +
                                "check for capitalization and other typos.")


    ## Exclude inappropriate combinations of method an distance
    if method == 'ball_tree' and (distance == 'cosine'
                                  or distance == _turicreate.distances.cosine
                                  or distance == 'dot_product'
                                  or distance == _turicreate.distances.dot_product
                                  or distance == 'transformed_dot_product'
                                  or distance == _turicreate.distances.transformed_dot_product):
        raise TypeError("The ball tree method does not work with 'cosine' " +
                        "'dot_product', or 'transformed_dot_product' distance." +
                        "Please use the 'brute_force' method for these distances.")


    if method == 'lsh' and ('num_projections_per_table' not in _method_options):
        if distance == 'jaccard' or distance == _turicreate.distances.jaccard:
            _method_options['num_projections_per_table'] = 4
        elif distance == 'cosine' or distance == _turicreate.distances.cosine:
            _method_options['num_projections_per_table'] = 16
        else:
            _method_options['num_projections_per_table'] = 8

    ## Initial validation and processing of the label
    if label is None:
        _label = _robust_column_name('__id', dataset.column_names())
        _dataset = dataset.add_row_number(_label)
    else:
        _label = label
        _dataset = _copy.copy(dataset)

    col_type_map = {c:_dataset[c].dtype for c in _dataset.column_names()}
    _validate_row_label(_label, col_type_map)
    ref_labels = _dataset[_label]


    ## Determine the internal list of available feature names (may still include
    #  the row label name).
    if features is None:
        _features = _dataset.column_names()
    else:
        _features = _copy.deepcopy(features)


    ## Check if there's only one feature and it's the same as the row label.
    #  This would also be trapped by the composite distance validation, but the
    #  error message is not very informative for the user.
    free_features = set(_features).difference([_label])
    if len(free_features) < 1:
        raise _ToolkitError("The only available feature is the same as the " +
                            "row label column. Please specify features " +
                            "that are not also row labels.")


    ### Validate and preprocess the distance function
    ### ---------------------------------------------
    # - The form of the 'distance' controls how we interact with the 'features'
    #   parameter as well.
    # - At this point, the row label 'label' may still be in the list(s) of
    #   features.

    ## Convert any distance function input into a single composite distance.
    # distance is already a composite distance
    if isinstance(distance, list):
        distance = _copy.deepcopy(distance)

    # distance is a single name (except 'auto') or function handle.
    elif (hasattr(distance, '__call__') or
        (isinstance(distance, str) and not distance == 'auto')):
        distance = [[_features, distance, 1]]

    # distance is unspecified and needs to be constructed.
    elif distance is None or distance == 'auto':
        sample = _dataset.head()
        distance = _construct_auto_distance(_features,
                                            _dataset.column_names(),
                                            _dataset.column_types(),
                                            sample)

    else:
        raise TypeError("Input 'distance' not understood. The 'distance' "
                        " argument must be a string, function handle, or " +
                        "composite distance.")

    ## Basic composite distance validation, remove the row label from all
    #  feature lists, and convert string distance names into distance functions.
    distance = _scrub_composite_distance_features(distance, [_label])
    distance = _convert_distance_names_to_functions(distance)
    _validate_composite_distance(distance)

    ## Raise an error if any distances are used with non-lists
    list_features_to_check = []
    sparse_distances = ['jaccard', 'weighted_jaccard', 'cosine', 'dot_product', 'transformed_dot_product']
    sparse_distances = [_turicreate.distances.__dict__[k] for k in sparse_distances]
    for d in distance:
        feature_names, dist, _ = d
        list_features = [f for f in feature_names if _dataset[f].dtype == list]
        for f in list_features:
            if dist in sparse_distances:
                list_features_to_check.append(f)
            else:
                raise TypeError("The chosen distance cannot currently be used " +
                                "on list-typed columns.")
    for f in list_features_to_check:
        only_str_lists = _validate_lists(_dataset[f], [str])
        if not only_str_lists:
            raise TypeError("Distances for sparse data, such as jaccard " +
                            "and weighted_jaccard, can only be used on " +
                            "lists containing only strings. Please modify " +
                            "any list features accordingly before creating " +
                            "the nearest neighbors model.")

    ## Raise an error if any component has string features are in single columns
    for d in distance:
        feature_names, dist, _ = d

        if (len(feature_names) > 1) and (dist == _turicreate.distances.levenshtein):
            raise ValueError("Levenshtein distance cannot be used with multiple " +
                             "columns. Please concatenate strings into a single " +
                             "column before creating the nearest neighbors model.")

    ## Get the union of feature names and make a clean dataset.
    clean_features = _get_composite_distance_features(distance)
    sf_clean = _tkutl._toolkits_select_columns(_dataset, clean_features)


    ## Decide which method to use
    ## - If more than one distance component (specified either directly or
    #  generated automatically because distance set to 'auto'), then do brute
    #  force.
    if len(distance) > 1:
        _method = 'brute_force'

        if method != 'brute_force' and verbose is True:
            print("Defaulting to brute force instead of ball tree because " +\
                "there are multiple distance components.")

    else:
        if method == 'auto':

            # get the total number of variables. Assume the number of elements in
            # array type columns does not change
            num_variables = sum([len(x) if hasattr(x, '__iter__') else 1
                for x in _six.itervalues(sf_clean[0])])

            # flag if all the features in the single composite are of numeric
            # type.
            numeric_type_flag = all([x in [int, float, list, array.array]
                for x in sf_clean.column_types()])

            ## Conditions necessary for ball tree to work and be worth it
            if ((distance[0][1] in ['euclidean',
                                    'manhattan',
                                    _turicreate.distances.euclidean,
                                    _turicreate.distances.manhattan])
                    and numeric_type_flag is True
                    and num_variables <= 200):

                    _method = 'ball_tree'

            else:
                _method = 'brute_force'

        else:
            _method = method


    ## Pick the right model name for the method
    if _method == 'ball_tree':
        model_name = 'nearest_neighbors_ball_tree'

    elif _method == 'brute_force':
        model_name = 'nearest_neighbors_brute_force'

    elif _method == 'lsh':
        model_name = 'nearest_neighbors_lsh'

    else:
        raise ValueError("Method must be 'auto', 'ball_tree', 'brute_force', " +
                         "or 'lsh'.")


    ## Package the model options
    opts = {}
    opts.update(_method_options)
    opts.update(
        {'model_name': model_name,
        'ref_labels': ref_labels,
        'label': label,
        'sf_features': sf_clean,
        'composite_params': distance})

    ## Construct the nearest neighbors model
    with QuietProgress(verbose):
        result = _turicreate.extensions._nearest_neighbors.train(opts)

    model_proxy = result['model']
    model = NearestNeighborsModel(model_proxy)

    return model