def _assert_all_loadable_terms_specialized_to(self, domain):
        """Make sure that we've specialized all loadable terms in the graph.
        """
        for term in self.graph.node:
            if isinstance(term, LoadableTerm):
                assert term.domain is domain