def add_api_compression(self, api_id, min_compression_size):
        """
        Add Rest API compression
        """
        self.apigateway_client.update_rest_api(
            restApiId=api_id,
            patchOperations=[
                {
                    'op': 'replace',
                    'path': '/minimumCompressionSize',
                    'value': str(min_compression_size)
                }
            ]
        )