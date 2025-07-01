def get_params():
    ''' Get parameters from command line '''
    parser = argparse.ArgumentParser()
    parser.add_argument("--data_dir", type=str, default='/tmp/tensorflow/mnist/input_data', help="data directory")
    parser.add_argument("--dropout_rate", type=float, default=0.5, help="dropout rate")
    parser.add_argument("--channel_1_num", type=int, default=32)
    parser.add_argument("--channel_2_num", type=int, default=64)
    parser.add_argument("--conv_size", type=int, default=5)
    parser.add_argument("--pool_size", type=int, default=2)
    parser.add_argument("--hidden_size", type=int, default=1024)
    parser.add_argument("--learning_rate", type=float, default=1e-4)
    parser.add_argument("--batch_num", type=int, default=2700)
    parser.add_argument("--batch_size", type=int, default=32)

    args, _ = parser.parse_known_args()
    return args