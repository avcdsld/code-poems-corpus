def QA_fetch_get_hkindex_list(ip=None, port=None):
    """[summary]

    Keyword Arguments:
        ip {[type]} -- [description] (default: {None})
        port {[type]} -- [description] (default: {None})

# 港股 HKMARKET
       27         5      香港指数         FH
       31         2      香港主板         KH
       48         2     香港创业板         KG
       49         2      香港基金         KT
       43         1     B股转H股         HB

    """

    global extension_market_list
    extension_market_list = QA_fetch_get_extensionmarket_list(
    ) if extension_market_list is None else extension_market_list

    return extension_market_list.query('market==27')