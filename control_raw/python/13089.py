def parse_rev_args(receive_msg):
    """ parse reveive msgs to global variable
    """
    global trainloader
    global testloader
    global net
    global criterion
    global optimizer

    # Loading Data
    logger.debug("Preparing data..")

    transform_train, transform_test = utils.data_transforms_cifar10(args)

    trainset = torchvision.datasets.CIFAR10(
        root="./data", train=True, download=True, transform=transform_train
    )
    trainloader = torch.utils.data.DataLoader(
        trainset, batch_size=args.batch_size, shuffle=True, num_workers=2
    )

    testset = torchvision.datasets.CIFAR10(
        root="./data", train=False, download=True, transform=transform_test
    )
    testloader = torch.utils.data.DataLoader(
        testset, batch_size=args.batch_size, shuffle=False, num_workers=2
    )

    # Model
    logger.debug("Building model..")
    net = build_graph_from_json(receive_msg)

    net = net.to(device)
    criterion = nn.CrossEntropyLoss()
    if device == "cuda" and torch.cuda.device_count() > 1:
        net = torch.nn.DataParallel(net)

    if args.optimizer == "SGD":
        optimizer = optim.SGD(
            net.parameters(), lr=args.learning_rate, momentum=0.9, weight_decay=5e-4
        )
    if args.optimizer == "Adadelta":
        optimizer = optim.Adadelta(net.parameters(), lr=args.learning_rate)
    if args.optimizer == "Adagrad":
        optimizer = optim.Adagrad(net.parameters(), lr=args.learning_rate)
    if args.optimizer == "Adam":
        optimizer = optim.Adam(net.parameters(), lr=args.learning_rate)
    if args.optimizer == "Adamax":
        optimizer = optim.Adamax(net.parameters(), lr=args.learning_rate)
    if args.optimizer == "RMSprop":
        optimizer = optim.RMSprop(net.parameters(), lr=args.learning_rate)


    return 0