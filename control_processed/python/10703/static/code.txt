def run_algorithm(start,
                  end,
                  initialize,
                  capital_base,
                  handle_data=None,
                  before_trading_start=None,
                  analyze=None,
                  data_frequency='daily',
                  bundle='quantopian-quandl',
                  bundle_timestamp=None,
                  trading_calendar=None,
                  metrics_set='default',
                  benchmark_returns=None,
                  default_extension=True,
                  extensions=(),
                  strict_extensions=True,
                  environ=os.environ,
                  blotter='default'):
    """
    Run a trading algorithm.

    Parameters
    ----------
    start : datetime
        The start date of the backtest.
    end : datetime
        The end date of the backtest..
    initialize : callable[context -> None]
        The initialize function to use for the algorithm. This is called once
        at the very begining of the backtest and should be used to set up
        any state needed by the algorithm.
    capital_base : float
        The starting capital for the backtest.
    handle_data : callable[(context, BarData) -> None], optional
        The handle_data function to use for the algorithm. This is called
        every minute when ``data_frequency == 'minute'`` or every day
        when ``data_frequency == 'daily'``.
    before_trading_start : callable[(context, BarData) -> None], optional
        The before_trading_start function for the algorithm. This is called
        once before each trading day (after initialize on the first day).
    analyze : callable[(context, pd.DataFrame) -> None], optional
        The analyze function to use for the algorithm. This function is called
        once at the end of the backtest and is passed the context and the
        performance data.
    data_frequency : {'daily', 'minute'}, optional
        The data frequency to run the algorithm at.
    bundle : str, optional
        The name of the data bundle to use to load the data to run the backtest
        with. This defaults to 'quantopian-quandl'.
    bundle_timestamp : datetime, optional
        The datetime to lookup the bundle data for. This defaults to the
        current time.
    trading_calendar : TradingCalendar, optional
        The trading calendar to use for your backtest.
    metrics_set : iterable[Metric] or str, optional
        The set of metrics to compute in the simulation. If a string is passed,
        resolve the set with :func:`zipline.finance.metrics.load`.
    default_extension : bool, optional
        Should the default zipline extension be loaded. This is found at
        ``$ZIPLINE_ROOT/extension.py``
    extensions : iterable[str], optional
        The names of any other extensions to load. Each element may either be
        a dotted module path like ``a.b.c`` or a path to a python file ending
        in ``.py`` like ``a/b/c.py``.
    strict_extensions : bool, optional
        Should the run fail if any extensions fail to load. If this is false,
        a warning will be raised instead.
    environ : mapping[str -> str], optional
        The os environment to use. Many extensions use this to get parameters.
        This defaults to ``os.environ``.
    blotter : str or zipline.finance.blotter.Blotter, optional
        Blotter to use with this algorithm. If passed as a string, we look for
        a blotter construction function registered with
        ``zipline.extensions.register`` and call it with no parameters.
        Default is a :class:`zipline.finance.blotter.SimulationBlotter` that
        never cancels orders.

    Returns
    -------
    perf : pd.DataFrame
        The daily performance of the algorithm.

    See Also
    --------
    zipline.data.bundles.bundles : The available data bundles.
    """
    load_extensions(default_extension, extensions, strict_extensions, environ)

    return _run(
        handle_data=handle_data,
        initialize=initialize,
        before_trading_start=before_trading_start,
        analyze=analyze,
        algofile=None,
        algotext=None,
        defines=(),
        data_frequency=data_frequency,
        capital_base=capital_base,
        bundle=bundle,
        bundle_timestamp=bundle_timestamp,
        start=start,
        end=end,
        output=os.devnull,
        trading_calendar=trading_calendar,
        print_algo=False,
        metrics_set=metrics_set,
        local_namespace=False,
        environ=environ,
        blotter=blotter,
        benchmark_returns=benchmark_returns,
    )