def from_api_repr(cls, resource, bucket):
        """Construct an instance from the JSON repr returned by the server.

        See: https://cloud.google.com/storage/docs/json_api/v1/notifications

        :type resource: dict
        :param resource: JSON repr of the notification

        :type bucket: :class:`google.cloud.storage.bucket.Bucket`
        :param bucket: Bucket to which the notification is bound.

        :rtype: :class:`BucketNotification`
        :returns: the new notification instance
        """
        topic_path = resource.get("topic")
        if topic_path is None:
            raise ValueError("Resource has no topic")

        name, project = _parse_topic_path(topic_path)
        instance = cls(bucket, name, topic_project=project)
        instance._properties = resource

        return instance