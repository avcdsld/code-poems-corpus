def create_stack_template(  self,
                                lambda_arn,
                                lambda_name,
                                api_key_required,
                                iam_authorization,
                                authorizer,
                                cors_options=None,
                                description=None,
                                endpoint_configuration=None
                            ):
        """
        Build the entire CF stack.
        Just used for the API Gateway, but could be expanded in the future.
        """

        auth_type = "NONE"
        if iam_authorization and authorizer:
            logger.warn("Both IAM Authorization and Authorizer are specified, this is not possible. "
                        "Setting Auth method to IAM Authorization")
            authorizer = None
            auth_type = "AWS_IAM"
        elif iam_authorization:
            auth_type = "AWS_IAM"
        elif authorizer:
            auth_type = authorizer.get("type", "CUSTOM")

        # build a fresh template
        self.cf_template = troposphere.Template()
        self.cf_template.add_description('Automatically generated with Zappa')
        self.cf_api_resources = []
        self.cf_parameters = {}

        restapi = self.create_api_gateway_routes(
                                            lambda_arn,
                                            api_name=lambda_name,
                                            api_key_required=api_key_required,
                                            authorization_type=auth_type,
                                            authorizer=authorizer,
                                            cors_options=cors_options,
                                            description=description,
                                            endpoint_configuration=endpoint_configuration
                                        )
        return self.cf_template