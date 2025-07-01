def app_profile(
        self,
        app_profile_id,
        routing_policy_type=None,
        description=None,
        cluster_id=None,
        allow_transactional_writes=None,
    ):
        """Factory to create AppProfile associated with this instance.

        For example:

        .. literalinclude:: snippets.py
            :start-after: [START bigtable_create_app_profile]
            :end-before: [END bigtable_create_app_profile]

        :type app_profile_id: str
        :param app_profile_id: The ID of the AppProfile. Must be of the form
                               ``[_a-zA-Z0-9][-_.a-zA-Z0-9]*``.

        :type: routing_policy_type: int
        :param: routing_policy_type: The type of the routing policy.
                                     Possible values are represented
                                     by the following constants:
                                     :data:`google.cloud.bigtable.enums.RoutingPolicyType.ANY`
                                     :data:`google.cloud.bigtable.enums.RoutingPolicyType.SINGLE`

        :type: description: str
        :param: description: (Optional) Long form description of the use
                             case for this AppProfile.

        :type: cluster_id: str
        :param: cluster_id: (Optional) Unique cluster_id which is only required
                            when routing_policy_type is
                            ROUTING_POLICY_TYPE_SINGLE.

        :type: allow_transactional_writes: bool
        :param: allow_transactional_writes: (Optional) If true, allow
                                            transactional writes for
                                            ROUTING_POLICY_TYPE_SINGLE.

        :rtype: :class:`~google.cloud.bigtable.app_profile.AppProfile>`
        :returns: AppProfile for this instance.
        """
        return AppProfile(
            app_profile_id,
            self,
            routing_policy_type=routing_policy_type,
            description=description,
            cluster_id=cluster_id,
            allow_transactional_writes=allow_transactional_writes,
        )