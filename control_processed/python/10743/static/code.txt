def make_simple_multi_country_equity_info(countries_to_sids,
                                          countries_to_exchanges,
                                          start_date,
                                          end_date):
    """Create a DataFrame representing assets that exist for the full duration
    between `start_date` and `end_date`, from multiple countries.
    """
    sids = []
    symbols = []
    exchanges = []

    for country, country_sids in countries_to_sids.items():
        exchange = countries_to_exchanges[country]
        for i, sid in enumerate(country_sids):
            sids.append(sid)
            symbols.append('-'.join([country, str(i)]))
            exchanges.append(exchange)

    return pd.DataFrame(
        {
            'symbol': symbols,
            'start_date': start_date,
            'end_date': end_date,
            'asset_name': symbols,
            'exchange': exchanges,
        },
        index=sids,
        columns=(
            'start_date',
            'end_date',
            'symbol',
            'exchange',
            'asset_name',
        ),
    )