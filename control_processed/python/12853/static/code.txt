def train(args, params):
    '''
    Train model
    '''
    x_train, y_train, x_test, y_test = load_mnist_data(args)
    model = create_mnist_model(params)

    # nni 
    model.fit(x_train, y_train, batch_size=args.batch_size, epochs=args.epochs, verbose=1,
        validation_data=(x_test, y_test), callbacks=[SendMetrics(), TensorBoard(log_dir=TENSORBOARD_DIR)])

    _, acc = model.evaluate(x_test, y_test, verbose=0)
    LOG.debug('Final result is: %d', acc)
    nni.report_final_result(acc)