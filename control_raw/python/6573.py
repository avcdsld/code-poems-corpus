def iterate(self, resource_type=None):
        """
        Iterate over all resources within the SAM template, optionally filtering by type

        :param string resource_type: Optional type to filter the resources by
        :yields (string, SamResource): Tuple containing LogicalId and the resource
        """

        for logicalId, resource_dict in self.resources.items():

            resource = SamResource(resource_dict)
            needs_filter = resource.valid()
            if resource_type:
                needs_filter = needs_filter and resource.type == resource_type

            if needs_filter:
                yield logicalId, resource