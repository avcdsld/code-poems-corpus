def train(args):
    """Training helper."""
    if not args.model.lower() in ['cbow', 'skipgram']:
        logging.error('Unsupported model %s.', args.model)
        sys.exit(1)

    if args.data.lower() == 'toy':
        data = mx.gluon.data.SimpleDataset(nlp.data.Text8(segment='train')[:2])
        data, vocab, idx_to_counts = preprocess_dataset(
            data, max_vocab_size=args.max_vocab_size)
    elif args.data.lower() == 'text8':
        data = nlp.data.Text8(segment='train')
        data, vocab, idx_to_counts = preprocess_dataset(
            data, max_vocab_size=args.max_vocab_size)
    elif args.data.lower() == 'fil9':
        data = nlp.data.Fil9(max_sentence_length=10000)
        data, vocab, idx_to_counts = preprocess_dataset(
            data, max_vocab_size=args.max_vocab_size)
    elif args.data.lower() == 'wiki':
        data, vocab, idx_to_counts = wiki(args.wiki_root, args.wiki_date,
                                          args.wiki_language,
                                          args.max_vocab_size)

    if args.ngram_buckets > 0:
        data, batchify_fn, subword_function = transform_data_fasttext(
            data, vocab, idx_to_counts, cbow=args.model.lower() == 'cbow',
            ngram_buckets=args.ngram_buckets, ngrams=args.ngrams,
            batch_size=args.batch_size, window_size=args.window,
            frequent_token_subsampling=args.frequent_token_subsampling)
    else:
        subword_function = None
        data, batchify_fn = transform_data_word2vec(
            data, vocab, idx_to_counts, cbow=args.model.lower() == 'cbow',
            batch_size=args.batch_size, window_size=args.window,
            frequent_token_subsampling=args.frequent_token_subsampling)

    num_tokens = float(sum(idx_to_counts))

    model = CBOW if args.model.lower() == 'cbow' else SG
    embedding = model(token_to_idx=vocab.token_to_idx, output_dim=args.emsize,
                      batch_size=args.batch_size, num_negatives=args.negative,
                      negatives_weights=mx.nd.array(idx_to_counts),
                      subword_function=subword_function)
    context = get_context(args)
    embedding.initialize(ctx=context)
    if not args.no_hybridize:
        embedding.hybridize(static_alloc=True, static_shape=True)

    optimizer_kwargs = dict(learning_rate=args.lr)
    try:
        trainer = mx.gluon.Trainer(embedding.collect_params(), args.optimizer,
                                   optimizer_kwargs)
    except ValueError as e:
        if args.optimizer == 'groupadagrad':
            logging.warning('MXNet <= v1.3 does not contain '
                            'GroupAdaGrad support. Falling back to AdaGrad')
            trainer = mx.gluon.Trainer(embedding.collect_params(), 'adagrad',
                                       optimizer_kwargs)
        else:
            raise e

    try:
        if args.no_prefetch_batch:
            data = data.transform(batchify_fn)
        else:
            from executors import LazyThreadPoolExecutor
            num_cpu = len(os.sched_getaffinity(0))
            ex = LazyThreadPoolExecutor(num_cpu)
    except (ImportError, SyntaxError, AttributeError):
        # Py2 - no async prefetching is supported
        logging.warning(
            'Asynchronous batch prefetching is not supported on Python 2. '
            'Consider upgrading to Python 3 for improved performance.')
        data = data.transform(batchify_fn)

    num_update = 0
    prefetched_iters = []
    for _ in range(min(args.num_prefetch_epoch, args.epochs)):
        prefetched_iters.append(iter(data))
    for epoch in range(args.epochs):
        if epoch + len(prefetched_iters) < args.epochs:
            prefetched_iters.append(iter(data))
        data_iter = prefetched_iters.pop(0)
        try:
            batches = ex.map(batchify_fn, data_iter)
        except NameError:  # Py 2 or batch prefetching disabled
            batches = data_iter

        # Logging variables
        log_wc = 0
        log_start_time = time.time()
        log_avg_loss = 0

        for i, batch in enumerate(batches):
            ctx = context[i % len(context)]
            batch = [array.as_in_context(ctx) for array in batch]
            with mx.autograd.record():
                loss = embedding(*batch)
            loss.backward()

            num_update += loss.shape[0]
            if len(context) == 1 or (i + 1) % len(context) == 0:
                trainer.step(batch_size=1)

            # Logging
            log_wc += loss.shape[0]
            log_avg_loss += loss.mean().as_in_context(context[0])
            if (i + 1) % args.log_interval == 0:
                # Forces waiting for computation by computing loss value
                log_avg_loss = log_avg_loss.asscalar() / args.log_interval
                wps = log_wc / (time.time() - log_start_time)
                # Due to subsampling, the overall number of batches is an upper
                # bound
                num_batches = num_tokens // args.batch_size
                if args.model.lower() == 'skipgram':
                    num_batches = (num_tokens * args.window * 2) // args.batch_size
                else:
                    num_batches = num_tokens // args.batch_size
                logging.info('[Epoch {} Batch {}/{}] loss={:.4f}, '
                             'throughput={:.2f}K wps, wc={:.2f}K'.format(
                                 epoch, i + 1, num_batches, log_avg_loss,
                                 wps / 1000, log_wc / 1000))
                log_start_time = time.time()
                log_avg_loss = 0
                log_wc = 0

            if args.eval_interval and (i + 1) % args.eval_interval == 0:
                with print_time('mx.nd.waitall()'):
                    mx.nd.waitall()
                with print_time('evaluate'):
                    evaluate(args, embedding, vocab, num_update)

    # Evaluate
    with print_time('mx.nd.waitall()'):
        mx.nd.waitall()
    with print_time('evaluate'):
        evaluate(args, embedding, vocab, num_update,
                 eval_analogy=not args.no_eval_analogy)

    # Save params
    with print_time('save parameters'):
        embedding.save_parameters(os.path.join(args.logdir, 'embedding.params'))