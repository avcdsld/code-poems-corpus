def _get_logits_name(self):
    """
    Looks for the name of the layer producing the logits.
    :return: name of layer producing the logits
    """
    softmax_name = self._get_softmax_name()
    softmax_layer = self.model.get_layer(softmax_name)

    if not isinstance(softmax_layer, Activation):
      # In this case, the activation is part of another layer
      return softmax_name

    if not hasattr(softmax_layer, '_inbound_nodes'):
      raise RuntimeError("Please update keras to version >= 2.1.3")

    node = softmax_layer._inbound_nodes[0]

    logits_name = node.inbound_layers[0].name

    return logits_name