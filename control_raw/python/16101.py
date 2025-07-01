def add_enumerated_multiarray_shapes(spec, feature_name, shapes):
    """
    Annotate an input or output multiArray feature in a Neural Network spec to
    to accommodate a list of enumerated array shapes

    :param spec: MLModel
        The MLModel spec containing the feature

    :param feature_name: str
        The name of the image feature for which to add shape information.
        If the feature is not found in the input or output descriptions then
        an exception is thrown

    :param shapes: [] | NeuralNetworkMultiArrayShape
        A single or a list of NeuralNetworkImageSize objects which encode valid
        size information for a image feature

    Examples
    --------
    .. sourcecode:: python

        >>> import coremltools
        >>> from coremltools.models.neural_network import flexible_shape_utils
        >>> spec = coremltools.utils.load_spec('mymodel.mlmodel')
        >>> array_shapes = [flexible_shape_utils.NeuralNetworkMultiArrayShape(3)]
        >>> second_shape = flexible_shape_utils.NeuralNetworkMultiArrayShape()
        >>> second_shape.set_channel_shape(3)
        >>> second_shape.set_height_shape(10)
        >>> second_shape.set_width_shape(15)
        >>> array_shapes.append(second_shape)
        >>> flexible_shape_utils.add_enumerated_multiarray_shapes(spec, feature_name='my_multiarray_featurename', shapes=array_shapes)

    :return:
        None. The spec object is updated
    """

    if not isinstance(shapes, list):
        shapes = [shapes]

    for shape in shapes:
        if not isinstance(shape, NeuralNetworkMultiArrayShape):
            raise Exception(
                'Shape ranges should be of type NeuralNetworkMultiArrayShape')
        shape._validate_multiarray_shape()

    feature = _get_feature(spec, feature_name)
    if feature.type.WhichOneof('Type') != 'multiArrayType':
        raise Exception('Trying to add enumerated shapes to '
                        'a non-multiArray feature type')

    if feature.type.multiArrayType.WhichOneof(
            'ShapeFlexibility') != 'enumeratedShapes':
        feature.type.multiArrayType.ClearField('ShapeFlexibility')

    eshape_len = len(feature.type.multiArrayType.enumeratedShapes.shapes)

    # Add default array shape to list of enumerated shapes if enumerated shapes
    # field is currently empty
    if eshape_len == 0:
        fixed_shape = feature.type.multiArrayType.shape
        if len(fixed_shape) == 1:
            fs = NeuralNetworkMultiArrayShape(fixed_shape[0])
            shapes.append(fs)
        elif len(fixed_shape) == 3:
            fs = NeuralNetworkMultiArrayShape()
            fs.set_channel_shape(fixed_shape[0])
            fs.set_height_shape(fixed_shape[1])
            fs.set_width_shape(fixed_shape[2])
            shapes.append(fs)
        else:
            raise Exception('Original fixed multiArray shape for {} is invalid'
                            .format(feature_name))

    for shape in shapes:
        s = feature.type.multiArrayType.enumeratedShapes.shapes.add()
        s.shape.extend(shape.multiarray_shape)

    # Bump up specification version
    spec.specificationVersion = max(_MINIMUM_FLEXIBLE_SHAPES_SPEC_VERSION,
                                    spec.specificationVersion)