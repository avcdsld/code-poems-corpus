def add_lifecycle_delete_rule(self, **kw):
        """Add a "delete" rule to lifestyle rules configured for this bucket.

        See https://cloud.google.com/storage/docs/lifecycle and
             https://cloud.google.com/storage/docs/json_api/v1/buckets

        .. literalinclude:: snippets.py
          :start-after: [START add_lifecycle_delete_rule]
          :end-before: [END add_lifecycle_delete_rule]

        :type kw: dict
        :params kw: arguments passed to :class:`LifecycleRuleConditions`.
        """
        rules = list(self.lifecycle_rules)
        rules.append(LifecycleRuleDelete(**kw))
        self.lifecycle_rules = rules