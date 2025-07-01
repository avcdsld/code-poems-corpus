def k_fold_cross_valid(k, epochs, verbose_epoch, X_train, y_train,
                       learning_rate, weight_decay, batch_size):
    """Conducts k-fold cross validation for the model."""
    assert k > 1
    fold_size = X_train.shape[0] // k

    train_loss_sum = 0.0
    test_loss_sum = 0.0
    for test_idx in range(k):
        X_val_test = X_train[test_idx * fold_size: (test_idx + 1) *
                                                   fold_size, :]
        y_val_test = y_train[test_idx * fold_size: (test_idx + 1) * fold_size]
        val_train_defined = False
        for i in range(k):
            if i != test_idx:
                X_cur_fold = X_train[i * fold_size: (i + 1) * fold_size, :]
                y_cur_fold = y_train[i * fold_size: (i + 1) * fold_size]
                if not val_train_defined:
                    X_val_train = X_cur_fold
                    y_val_train = y_cur_fold
                    val_train_defined = True
                else:
                    X_val_train = nd.concat(X_val_train, X_cur_fold, dim=0)
                    y_val_train = nd.concat(y_val_train, y_cur_fold, dim=0)
        net = get_net()
        train_loss = train(net, X_val_train, y_val_train, epochs, verbose_epoch,
                           learning_rate, weight_decay, batch_size)
        train_loss_sum += train_loss
        test_loss = get_rmse_log(net, X_val_test, y_val_test)
        print("Test loss: %f" % test_loss)
        test_loss_sum += test_loss
    return train_loss_sum / k, test_loss_sum / k