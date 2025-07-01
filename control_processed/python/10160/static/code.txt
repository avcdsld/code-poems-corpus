def add_option(self, opts, dest, action=None, nargs=1, const=None,
                   obj=None):
        """Adds a new option named `dest` to the parser.  The destination
        is not inferred (unlike with optparse) and needs to be explicitly
        provided.  Action can be any of ``store``, ``store_const``,
        ``append``, ``appnd_const`` or ``count``.

        The `obj` can be used to identify the option in the order list
        that is returned from the parser.
        """
        if obj is None:
            obj = dest
        opts = [normalize_opt(opt, self.ctx) for opt in opts]
        option = Option(opts, dest, action=action, nargs=nargs,
                        const=const, obj=obj)
        self._opt_prefixes.update(option.prefixes)
        for opt in option._short_opts:
            self._short_opt[opt] = option
        for opt in option._long_opts:
            self._long_opt[opt] = option