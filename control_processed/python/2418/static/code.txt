def split_by_rand_pct(self, valid_pct:float=0.2, seed:int=None)->'ItemLists':
        "Split the items randomly by putting `valid_pct` in the validation set, optional `seed` can be passed."
        if valid_pct==0.: return self.split_none()
        if seed is not None: np.random.seed(seed)
        rand_idx = np.random.permutation(range_of(self))
        cut = int(valid_pct * len(self))
        return self.split_by_idx(rand_idx[:cut])