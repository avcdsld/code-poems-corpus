def call_for_each_tower(self, tower_fn):
        """
        Call the function `tower_fn` under :class:`TowerContext` for each tower.

        Returns:
            a list, contains the return values of `tower_fn` on each tower.
        """
        # if tower_fn returns [(grad, var), ...], this returns #GPU x #VAR x 2
        return DataParallelBuilder.build_on_towers(
            self.towers,
            tower_fn,
            # use no variable scope for the first tower
            use_vs=[False] + [True] * (len(self.towers) - 1))