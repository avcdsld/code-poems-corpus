def largest_indices(arr, n):
        "Returns the `n` largest indices from a numpy array `arr`."
        #https://stackoverflow.com/questions/6910641/how-do-i-get-indices-of-n-maximum-values-in-a-numpy-array
        flat = arr.flatten()
        indices = np.argpartition(flat, -n)[-n:]
        indices = indices[np.argsort(-flat[indices])]
        return np.unravel_index(indices, arr.shape)