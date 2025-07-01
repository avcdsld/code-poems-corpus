def _serve_experiments(self, request):
    """Serve a JSON array of experiments. Experiments are ordered by experiment
    started time (aka first event time) with empty times sorted last, and then
    ties are broken by sorting on the experiment name.
    """
    results = self.list_experiments_impl()
    return http_util.Respond(request, results, 'application/json')