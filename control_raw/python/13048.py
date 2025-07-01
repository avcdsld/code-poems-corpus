def data_transforms_mnist(args, mnist_mean=None, mnist_std=None):
    """ data_transforms for mnist dataset
    """
    if mnist_mean is None:
        mnist_mean = [0.5]

    if mnist_std is None:
        mnist_std = [0.5]

    train_transform = transforms.Compose(
        [
            transforms.RandomCrop(28, padding=4),
            transforms.RandomHorizontalFlip(),
            transforms.ToTensor(),
            transforms.Normalize(mnist_mean, mnist_std),
        ]
    )
    if args.cutout:
        train_transform.transforms.append(Cutout(args.cutout_length))

    valid_transform = transforms.Compose(
        [transforms.ToTensor(), transforms.Normalize(mnist_mean, mnist_std)]
    )
    return train_transform, valid_transform