def update_domain_name(self,
                           domain_name,
                           certificate_name=None,
                           certificate_body=None,
                           certificate_private_key=None,
                           certificate_chain=None,
                           certificate_arn=None,
                           lambda_name=None,
                           stage=None,
                           route53=True,
                           base_path=None):
        """
        This updates your certificate information for an existing domain,
        with similar arguments to boto's update_domain_name API Gateway api.

        It returns the resulting new domain information including the new certificate's ARN
        if created during this process.

        Previously, this method involved downtime that could take up to 40 minutes
        because the API Gateway api only allowed this by deleting, and then creating it.

        Related issues:     https://github.com/Miserlou/Zappa/issues/590
                            https://github.com/Miserlou/Zappa/issues/588
                            https://github.com/Miserlou/Zappa/pull/458
                            https://github.com/Miserlou/Zappa/issues/882
                            https://github.com/Miserlou/Zappa/pull/883
        """

        print("Updating domain name!")

        certificate_name = certificate_name + str(time.time())

        api_gateway_domain = self.apigateway_client.get_domain_name(domainName=domain_name)
        if not certificate_arn\
           and certificate_body and certificate_private_key and certificate_chain:
            acm_certificate = self.acm_client.import_certificate(Certificate=certificate_body,
                                                                 PrivateKey=certificate_private_key,
                                                                 CertificateChain=certificate_chain)
            certificate_arn = acm_certificate['CertificateArn']

        self.update_domain_base_path_mapping(domain_name, lambda_name, stage, base_path)

        return self.apigateway_client.update_domain_name(domainName=domain_name,
                                                         patchOperations=[
                                                             {"op" : "replace",
                                                              "path" : "/certificateName",
                                                              "value" : certificate_name},
                                                             {"op" : "replace",
                                                              "path" : "/certificateArn",
                                                              "value" : certificate_arn}
                                                         ])