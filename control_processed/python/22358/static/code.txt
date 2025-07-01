def register(self, subject, avro_schema):
        """
        POST /subjects/(string: subject)/versions
        Register a schema with the registry under the given subject
        and receive a schema id.

        avro_schema must be a parsed schema from the python avro library

        Multiple instances of the same schema will result in cache misses.

        :param str subject: subject name
        :param schema avro_schema: Avro schema to be registered
        :returns: schema_id
        :rtype: int
        """

        schemas_to_id = self.subject_to_schema_ids[subject]
        schema_id = schemas_to_id.get(avro_schema, None)
        if schema_id is not None:
            return schema_id
        # send it up
        url = '/'.join([self.url, 'subjects', subject, 'versions'])
        # body is { schema : json_string }

        body = {'schema': json.dumps(avro_schema.to_json())}
        result, code = self._send_request(url, method='POST', body=body)
        if (code == 401 or code == 403):
            raise ClientError("Unauthorized access. Error code:" + str(code))
        elif code == 409:
            raise ClientError("Incompatible Avro schema:" + str(code))
        elif code == 422:
            raise ClientError("Invalid Avro schema:" + str(code))
        elif not (code >= 200 and code <= 299):
            raise ClientError("Unable to register schema. Error code:" + str(code))
        # result is a dict
        schema_id = result['id']
        # cache it
        self._cache_schema(avro_schema, schema_id, subject)
        return schema_id