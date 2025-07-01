def _any_pandas_objects(terms):
    """Check a sequence of terms for instances of PandasObject."""
    return any(isinstance(term.value, pd.core.generic.PandasObject)
               for term in terms)