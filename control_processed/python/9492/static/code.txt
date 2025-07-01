def break_args_options(line):
    # type: (Text) -> Tuple[str, Text]
    """Break up the line into an args and options string.  We only want to shlex
    (and then optparse) the options, not the args.  args can contain markers
    which are corrupted by shlex.
    """
    tokens = line.split(' ')
    args = []
    options = tokens[:]
    for token in tokens:
        if token.startswith('-') or token.startswith('--'):
            break
        else:
            args.append(token)
            options.pop(0)
    return ' '.join(args), ' '.join(options)