def generate_random_sframe(num_rows, column_codes, random_seed = 0):
    """
    Creates a random SFrame with `num_rows` rows and randomly
    generated column types determined by `column_codes`.  The output
    SFrame is deterministic based on `random_seed`.
 
     `column_types` is a string with each character denoting one type
     of column, with the output SFrame having one column for each
     character in the string.  The legend is as follows:

        n:  numeric column, uniform 0-1 distribution. 
        N:  numeric column, uniform 0-1 distribution, 1% NaNs.
        r:  numeric column, uniform -100 to 100 distribution. 
        R:  numeric column, uniform -10000 to 10000 distribution, 1% NaNs.
        b:  binary integer column, uniform distribution
        z:  integer column with random integers between 1 and 10.
        Z:  integer column with random integers between 1 and 100.
        s:  categorical string column with 10 different unique short strings. 
        S:  categorical string column with 100 different unique short strings. 
        c:  categorical column with short string keys and 1000 unique values, triangle distribution.
        C:  categorical column with short string keys and 100000 unique values, triangle distribution.
        x:  categorical column with 128bit hex hashes and 1000 unique values. 
        X:  categorical column with 256bit hex hashes and 100000 unique values. 
        h:  column with unique 128bit hex hashes.
        H:  column with unique 256bit hex hashes.

        l:  categorical list with between 0 and 10 unique integer elements from a pool of 100 unique values. 
        L:  categorical list with between 0 and 100 unique integer elements from a pool of 1000 unique values.
        M:  categorical list with between 0 and 10 unique string elements from a pool of 100 unique values. 
        m:  categorical list with between 0 and 100 unique string elements from a pool of 1000 unique values.

        v:  numeric vector with 10 elements and uniform 0-1 elements.
        V:  numeric vector with 1000 elements and uniform 0-1 elements.
        w:  numeric vector with 10 elements and uniform 0-1 elements, 1% NANs.
        W:  numeric vector with 1000 elements and uniform 0-1 elements, 1% NANs.

        d: dictionary with with between 0 and 10 string keys from a
           pool of 100 unique keys, and random 0-1 values.

        D: dictionary with with between 0 and 100 string keys from a
           pool of 1000 unique keys, and random 0-1 values.

    For example::

      X = generate_random_sframe(10, 'nnv')

    will generate a 10 row SFrame with 2 floating point columns and
    one column of length 10 vectors.
    """

    from ..extensions import _generate_random_sframe

    assert isinstance(column_codes, str)
    assert isinstance(num_rows, int)
    assert isinstance(random_seed, int)
    
    X = _generate_random_sframe(num_rows, column_codes, random_seed, False, 0)
    X.__materialize__()
    return X