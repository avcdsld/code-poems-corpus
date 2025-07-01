def load_data_table(file,
                    index_col,
                    show_progress=False):
    """ Load data table from zip file provided by Quandl.
    """
    with ZipFile(file) as zip_file:
        file_names = zip_file.namelist()
        assert len(file_names) == 1, "Expected a single file from Quandl."
        wiki_prices = file_names.pop()
        with zip_file.open(wiki_prices) as table_file:
            if show_progress:
                log.info('Parsing raw data.')
            data_table = pd.read_csv(
                table_file,
                parse_dates=['date'],
                index_col=index_col,
                usecols=[
                    'ticker',
                    'date',
                    'open',
                    'high',
                    'low',
                    'close',
                    'volume',
                    'ex-dividend',
                    'split_ratio',
                ],
            )

    data_table.rename(
        columns={
            'ticker': 'symbol',
            'ex-dividend': 'ex_dividend',
        },
        inplace=True,
        copy=False,
    )
    return data_table