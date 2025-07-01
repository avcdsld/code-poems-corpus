def dataset_list(self,
                     sort_by=None,
                     size=None,
                     file_type=None,
                     license_name=None,
                     tag_ids=None,
                     search=None,
                     user=None,
                     mine=False,
                     page=1):
        """ return a list of datasets!

            Parameters
            ==========
            sort_by: how to sort the result, see valid_sort_bys for options
            size: the size of the dataset, see valid_sizes for string options
            file_type: the format, see valid_file_types for string options
            license_name: string descriptor for license, see valid_license_names
            tag_ids: tag identifiers to filter the search
            search: a search term to use (default is empty string)
            user: username to filter the search to
            mine: boolean if True, group is changed to "my" to return personal
            page: the page to return (default is 1)
        """
        valid_sort_bys = ['hottest', 'votes', 'updated', 'active', 'published']
        if sort_by and sort_by not in valid_sort_bys:
            raise ValueError('Invalid sort by specified. Valid options are ' +
                             str(valid_sort_bys))

        valid_sizes = ['all', 'small', 'medium', 'large']
        if size and size not in valid_sizes:
            raise ValueError('Invalid size specified. Valid options are ' +
                             str(valid_sizes))

        valid_file_types = ['all', 'csv', 'sqlite', 'json', 'bigQuery']
        if file_type and file_type not in valid_file_types:
            raise ValueError('Invalid file type specified. Valid options are '
                             + str(valid_file_types))

        valid_license_names = ['all', 'cc', 'gpl', 'odb', 'other']
        if license_name and license_name not in valid_license_names:
            raise ValueError('Invalid license specified. Valid options are ' +
                             str(valid_license_names))

        if int(page) <= 0:
            raise ValueError('Page number must be >= 1')

        group = 'public'
        if mine:
            group = 'my'
            if user:
                raise ValueError('Cannot specify both mine and a user')
        if user:
            group = 'user'

        datasets_list_result = self.process_response(
            self.datasets_list_with_http_info(
                group=group,
                sort_by=sort_by or 'hottest',
                size=size or 'all',
                filetype=file_type or 'all',
                license=license_name or 'all',
                tagids=tag_ids or '',
                search=search or '',
                user=user or '',
                page=page))
        return [Dataset(d) for d in datasets_list_result]