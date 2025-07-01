def quandl_bundle(environ,
                  asset_db_writer,
                  minute_bar_writer,
                  daily_bar_writer,
                  adjustment_writer,
                  calendar,
                  start_session,
                  end_session,
                  cache,
                  show_progress,
                  output_dir):
    """
    quandl_bundle builds a daily dataset using Quandl's WIKI Prices dataset.

    For more information on Quandl's API and how to obtain an API key,
    please visit https://docs.quandl.com/docs#section-authentication
    """
    api_key = environ.get('QUANDL_API_KEY')
    if api_key is None:
        raise ValueError(
            "Please set your QUANDL_API_KEY environment variable and retry."
        )

    raw_data = fetch_data_table(
        api_key,
        show_progress,
        environ.get('QUANDL_DOWNLOAD_ATTEMPTS', 5)
    )
    asset_metadata = gen_asset_metadata(
        raw_data[['symbol', 'date']],
        show_progress
    )
    asset_db_writer.write(asset_metadata)

    symbol_map = asset_metadata.symbol
    sessions = calendar.sessions_in_range(start_session, end_session)

    raw_data.set_index(['date', 'symbol'], inplace=True)
    daily_bar_writer.write(
        parse_pricing_and_vol(
            raw_data,
            sessions,
            symbol_map
        ),
        show_progress=show_progress
    )

    raw_data.reset_index(inplace=True)
    raw_data['symbol'] = raw_data['symbol'].astype('category')
    raw_data['sid'] = raw_data.symbol.cat.codes
    adjustment_writer.write(
        splits=parse_splits(
            raw_data[[
                'sid',
                'date',
                'split_ratio',
            ]].loc[raw_data.split_ratio != 1],
            show_progress=show_progress
        ),
        dividends=parse_dividends(
            raw_data[[
                'sid',
                'date',
                'ex_dividend',
            ]].loc[raw_data.ex_dividend != 0],
            show_progress=show_progress
        )
    )