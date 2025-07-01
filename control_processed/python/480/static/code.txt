def _equals(v1_indices, v1_values, v2_indices, v2_values):
        """
        Check equality between sparse/dense vectors,
        v1_indices and v2_indices assume to be strictly increasing.
        """
        v1_size = len(v1_values)
        v2_size = len(v2_values)
        k1 = 0
        k2 = 0
        all_equal = True
        while all_equal:
            while k1 < v1_size and v1_values[k1] == 0:
                k1 += 1
            while k2 < v2_size and v2_values[k2] == 0:
                k2 += 1

            if k1 >= v1_size or k2 >= v2_size:
                return k1 >= v1_size and k2 >= v2_size

            all_equal = v1_indices[k1] == v2_indices[k2] and v1_values[k1] == v2_values[k2]
            k1 += 1
            k2 += 1
        return all_equal