def _get_mps_od_net(input_image_shape, batch_size, output_size, anchors,
                    config, weights={}):
    """
    Initializes an MpsGraphAPI for object detection.
    """
    network = _MpsGraphAPI(network_id=_MpsGraphNetworkType.kODGraphNet)

    c_in, h_in, w_in =  input_image_shape
    c_out = output_size
    h_out = h_in // 32
    w_out = w_in // 32

    c_view = c_in
    h_view = h_in
    w_view = w_in

    network.init(batch_size, c_in, h_in, w_in, c_out, h_out, w_out,
                 weights=weights, config=config)
    return network