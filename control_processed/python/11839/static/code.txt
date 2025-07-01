def _combine_activations(
    layer1,
    layer2,
    activations1=None,
    activations2=None,
    mode=ActivationTranslation.BIDIRECTIONAL,
    number_activations=NUMBER_OF_AVAILABLE_SAMPLES,
):
    """Given two layers, combines their activations according to mode.

    ActivationTranslation.ONE_TO_TWO:
      Translate activations of layer1 into the space of layer2, and return a tuple of
      the translated activations and the original layer2 activations.

    ActivationTranslation.BIDIRECTIONAL:
      Translate activations of layer1 into the space of layer2, activations of layer2
      into the space of layer 1, concatenate them along their channels, and returns a
      tuple of the concatenated activations for each layer.
    """
    activations1 = activations1 or layer1.activations[:number_activations, ...]
    activations2 = activations2 or layer2.activations[:number_activations, ...]

    if mode is ActivationTranslation.ONE_TO_TWO:

        acts_1_to_2 = push_activations(activations1, layer1, layer2)
        return acts_1_to_2, activations2

    elif mode is ActivationTranslation.BIDIRECTIONAL:

        acts_1_to_2 = push_activations(activations1, layer1, layer2)
        acts_2_to_1 = push_activations(activations2, layer2, layer1)

        activations_model1 = np.concatenate((activations1, acts_1_to_2), axis=1)
        activations_model2 = np.concatenate((acts_2_to_1, activations2), axis=1)

        return activations_model1, activations_model2