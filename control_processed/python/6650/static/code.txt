def _depend_on_lambda_permissions(self, bucket, permission):
        """
        Make the S3 bucket depends on Lambda Permissions resource because when S3 adds a Notification Configuration,
        it will check whether it has permissions to access Lambda. This will fail if the Lambda::Permissions is not
        already applied for this bucket to invoke the Lambda.

        :param dict bucket: Dictionary representing the bucket in SAM template. This is a raw dictionary and not a
            "resource" object
        :param model.lambda_.lambda_permission permission: Lambda Permission resource that needs to be created before
            the bucket.
        :return: Modified Bucket dictionary
        """

        depends_on = bucket.get("DependsOn", [])

        # DependsOn can be either a list of strings or a scalar string
        if isinstance(depends_on, string_types):
            depends_on = [depends_on]

        depends_on_set = set(depends_on)
        depends_on_set.add(permission.logical_id)
        bucket["DependsOn"] = list(depends_on_set)

        return bucket