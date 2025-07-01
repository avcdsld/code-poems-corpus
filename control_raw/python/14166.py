def query_plan(self):
        """Return query plan from job statistics, if present.

        See:
        https://cloud.google.com/bigquery/docs/reference/rest/v2/jobs#statistics.query.queryPlan

        :rtype: list of :class:`QueryPlanEntry`
        :returns: mappings describing the query plan, or an empty list
                  if the query has not yet completed.
        """
        plan_entries = self._job_statistics().get("queryPlan", ())
        return [QueryPlanEntry.from_api_repr(entry) for entry in plan_entries]