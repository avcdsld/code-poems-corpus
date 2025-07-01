def _is_policy_template(self, policy):
        """
        Is the given policy data a policy template? Policy templates is a dictionary with one key which is the name
        of the template.

        :param dict policy: Policy data
        :return: True, if this is a policy template. False if it is not
        """

        return self._policy_template_processor is not None and \
            isinstance(policy, dict) and \
            len(policy) == 1 and \
            self._policy_template_processor.has(list(policy.keys())[0]) is True