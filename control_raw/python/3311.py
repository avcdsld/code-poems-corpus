def profile(model, inputs=None, n_texts=10000):
    """
    Profile a spaCy pipeline, to find out which functions take the most time.
    Input should be formatted as one JSON object per line with a key "text".
    It can either be provided as a JSONL file, or be read from sys.sytdin.
    If no input file is specified, the IMDB dataset is loaded via Thinc.
    """
    msg = Printer()
    if inputs is not None:
        inputs = _read_inputs(inputs, msg)
    if inputs is None:
        n_inputs = 25000
        with msg.loading("Loading IMDB dataset via Thinc..."):
            imdb_train, _ = thinc.extra.datasets.imdb()
            inputs, _ = zip(*imdb_train)
        msg.info("Loaded IMDB dataset and using {} examples".format(n_inputs))
        inputs = inputs[:n_inputs]
    with msg.loading("Loading model '{}'...".format(model)):
        nlp = load_model(model)
    msg.good("Loaded model '{}'".format(model))
    texts = list(itertools.islice(inputs, n_texts))
    cProfile.runctx("parse_texts(nlp, texts)", globals(), locals(), "Profile.prof")
    s = pstats.Stats("Profile.prof")
    msg.divider("Profile stats")
    s.strip_dirs().sort_stats("time").print_stats()