def get_training_data(batch_size):
    """ helper function to get dataloader"""
    return gluon.data.DataLoader(
        CIFAR10(train=True, transform=transformer),
        batch_size=batch_size, shuffle=True, last_batch='discard')