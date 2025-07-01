def map_predicate(self, f):
        """
        Map a function from str -> bool element-wise over ``self``.

        ``f`` will be applied exactly once to each non-missing unique value in
        ``self``. Missing values will always return False.
        """
        # Functions passed to this are of type str -> bool.  Don't ever call
        # them on None, which is the only non-str value we ever store in
        # categories.
        if self.missing_value is None:
            def f_to_use(x):
                return False if x is None else f(x)
        else:
            f_to_use = f

        # Call f on each unique value in our categories.
        results = np.vectorize(f_to_use, otypes=[bool_dtype])(self.categories)

        # missing_value should produce False no matter what
        results[self.reverse_categories[self.missing_value]] = False

        # unpack the results form each unique value into their corresponding
        # locations in our indices.
        return results[self.as_int_array()]