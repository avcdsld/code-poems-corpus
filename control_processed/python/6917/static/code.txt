def arch(args, seq_len=None):
    """
    define deep speech 2 network
    """
    if isinstance(args, argparse.Namespace):
        mode = args.config.get("common", "mode")
        is_bucketing = args.config.getboolean("arch", "is_bucketing")
        if mode == "train" or is_bucketing:
            channel_num = args.config.getint("arch", "channel_num")
            conv_layer1_filter_dim = \
                tuple(json.loads(args.config.get("arch", "conv_layer1_filter_dim")))
            conv_layer1_stride = tuple(json.loads(args.config.get("arch", "conv_layer1_stride")))
            conv_layer2_filter_dim = \
                tuple(json.loads(args.config.get("arch", "conv_layer2_filter_dim")))
            conv_layer2_stride = tuple(json.loads(args.config.get("arch", "conv_layer2_stride")))

            rnn_type = args.config.get("arch", "rnn_type")
            num_rnn_layer = args.config.getint("arch", "num_rnn_layer")
            num_hidden_rnn_list = json.loads(args.config.get("arch", "num_hidden_rnn_list"))

            is_batchnorm = args.config.getboolean("arch", "is_batchnorm")

            if seq_len is None:
                seq_len = args.config.getint('arch', 'max_t_count')

            num_label = args.config.getint('arch', 'max_label_length')

            num_rear_fc_layers = args.config.getint("arch", "num_rear_fc_layers")
            num_hidden_rear_fc_list = json.loads(args.config.get("arch", "num_hidden_rear_fc_list"))
            act_type_rear_fc_list = json.loads(args.config.get("arch", "act_type_rear_fc_list"))
            # model symbol generation
            # input preparation
            data = mx.sym.Variable('data')
            label = mx.sym.Variable('label')

            net = mx.sym.Reshape(data=data, shape=(-4, -1, 1, 0, 0))
            net = conv(net=net,
                       channels=channel_num,
                       filter_dimension=conv_layer1_filter_dim,
                       stride=conv_layer1_stride,
                       no_bias=is_batchnorm,
                       name='conv1')
            if is_batchnorm:
               # batch norm normalizes axis 1
               net = batchnorm(net, name="conv1_batchnorm")

            net = conv(net=net,
                       channels=channel_num,
                       filter_dimension=conv_layer2_filter_dim,
                       stride=conv_layer2_stride,
                       no_bias=is_batchnorm,
                       name='conv2')
            if is_batchnorm:
                # batch norm normalizes axis 1
                net = batchnorm(net, name="conv2_batchnorm")

            net = mx.sym.transpose(data=net, axes=(0, 2, 1, 3))
            net = mx.sym.Reshape(data=net, shape=(0, 0, -3))
            seq_len_after_conv_layer1 = int(
                math.floor((seq_len - conv_layer1_filter_dim[0]) / conv_layer1_stride[0])) + 1
            seq_len_after_conv_layer2 = int(
                math.floor((seq_len_after_conv_layer1 - conv_layer2_filter_dim[0])
                           / conv_layer2_stride[0])) + 1
            net = slice_symbol_to_seq_symobls(net=net, seq_len=seq_len_after_conv_layer2, axis=1)
            if rnn_type == "bilstm":
                net = bi_lstm_unroll(net=net,
                                     seq_len=seq_len_after_conv_layer2,
                                     num_hidden_lstm_list=num_hidden_rnn_list,
                                     num_lstm_layer=num_rnn_layer,
                                     dropout=0.,
                                     is_batchnorm=is_batchnorm,
                                     is_bucketing=is_bucketing)
            elif rnn_type == "gru":
                net = gru_unroll(net=net,
                                 seq_len=seq_len_after_conv_layer2,
                                 num_hidden_gru_list=num_hidden_rnn_list,
                                 num_gru_layer=num_rnn_layer,
                                 dropout=0.,
                                 is_batchnorm=is_batchnorm,
                                 is_bucketing=is_bucketing)
            elif rnn_type == "bigru":
                net = bi_gru_unroll(net=net,
                                    seq_len=seq_len_after_conv_layer2,
                                    num_hidden_gru_list=num_hidden_rnn_list,
                                    num_gru_layer=num_rnn_layer,
                                    dropout=0.,
                                    is_batchnorm=is_batchnorm,
                                    is_bucketing=is_bucketing)
            else:
                raise Exception('rnn_type should be one of the followings, bilstm,gru,bigru')

            # rear fc layers
            net = sequence_fc(net=net, seq_len=seq_len_after_conv_layer2,
                              num_layer=num_rear_fc_layers, prefix="rear",
                              num_hidden_list=num_hidden_rear_fc_list,
                              act_type_list=act_type_rear_fc_list,
                              is_batchnorm=is_batchnorm)
            # warpctc layer
            net = warpctc_layer(net=net,
                                seq_len=seq_len_after_conv_layer2,
                                label=label,
                                num_label=num_label,
                                character_classes_count=
                                (args.config.getint('arch', 'n_classes') + 1))
            args.config.set('arch', 'max_t_count', str(seq_len_after_conv_layer2))
            return net
        elif mode == 'load' or mode == 'predict':
            conv_layer1_filter_dim = \
                tuple(json.loads(args.config.get("arch", "conv_layer1_filter_dim")))
            conv_layer1_stride = tuple(json.loads(args.config.get("arch", "conv_layer1_stride")))
            conv_layer2_filter_dim = \
                tuple(json.loads(args.config.get("arch", "conv_layer2_filter_dim")))
            conv_layer2_stride = tuple(json.loads(args.config.get("arch", "conv_layer2_stride")))
            if seq_len is None:
                seq_len = args.config.getint('arch', 'max_t_count')
            seq_len_after_conv_layer1 = int(
                math.floor((seq_len - conv_layer1_filter_dim[0]) / conv_layer1_stride[0])) + 1
            seq_len_after_conv_layer2 = int(
                math.floor((seq_len_after_conv_layer1 - conv_layer2_filter_dim[0])
                           / conv_layer2_stride[0])) + 1

            args.config.set('arch', 'max_t_count', str(seq_len_after_conv_layer2))
        else:
            raise Exception('mode must be the one of the followings - train,predict,load')