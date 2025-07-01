def add_api_stage_to_api_key(self, api_key, api_id, stage_name):
        """
        Add api stage to Api key
        """
        self.apigateway_client.update_api_key(
            apiKey=api_key,
            patchOperations=[
                {
                    'op': 'add',
                    'path': '/stages',
                    'value': '{}/{}'.format(api_id, stage_name)
                }
            ]
        )