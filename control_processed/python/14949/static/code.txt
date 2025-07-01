def from_api_repr(cls, resource, zone):
        """Factory:  construct a record set given its API representation

        :type resource: dict
        :param resource: record sets representation returned from the API

        :type zone: :class:`google.cloud.dns.zone.ManagedZone`
        :param zone: A zone which holds one or more record sets.

        :rtype: :class:`google.cloud.dns.zone.ResourceRecordSet`
        :returns: RRS parsed from ``resource``.
        """
        name = resource["name"]
        record_type = resource["type"]
        ttl = int(resource["ttl"])
        rrdatas = resource["rrdatas"]
        return cls(name, record_type, ttl, rrdatas, zone=zone)