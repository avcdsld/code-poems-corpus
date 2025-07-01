def read_cluster_role_binding(self, name, **kwargs):
        """
        read the specified ClusterRoleBinding
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.read_cluster_role_binding(name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str name: name of the ClusterRoleBinding (required)
        :param str pretty: If 'true', then the output is pretty printed.
        :return: V1ClusterRoleBinding
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.read_cluster_role_binding_with_http_info(name, **kwargs)
        else:
            (data) = self.read_cluster_role_binding_with_http_info(name, **kwargs)
            return data