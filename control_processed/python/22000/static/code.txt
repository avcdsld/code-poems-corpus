def kernels_pull(self, kernel, path, metadata=False, quiet=True):
        """ pull a kernel, including a metadata file (if metadata is True)
            and associated files to a specified path.
             Parameters
            ==========
            kernel: the kernel to pull
            path: the path to pull files to on the filesystem
            metadata: if True, also pull metadata
            quiet: suppress verbosity (default is True)
        """
        existing_metadata = None
        if kernel is None:
            if path is None:
                existing_metadata_path = os.path.join(
                    os.getcwd(), self.KERNEL_METADATA_FILE)
            else:
                existing_metadata_path = os.path.join(
                    path, self.KERNEL_METADATA_FILE)
            if os.path.exists(existing_metadata_path):
                with open(existing_metadata_path) as f:
                    existing_metadata = json.load(f)
                    kernel = existing_metadata['id']
                    if 'INSERT_KERNEL_SLUG_HERE' in kernel:
                        raise ValueError('A kernel must be specified')
                    else:
                        print('Using kernel ' + kernel)

        if '/' in kernel:
            self.validate_kernel_string(kernel)
            kernel_url_list = kernel.split('/')
            owner_slug = kernel_url_list[0]
            kernel_slug = kernel_url_list[1]
        else:
            owner_slug = self.get_config_value(self.CONFIG_NAME_USER)
            kernel_slug = kernel

        if path is None:
            effective_path = self.get_default_download_dir(
                'kernels', owner_slug, kernel_slug)
        else:
            effective_path = path

        if not os.path.exists(effective_path):
            os.makedirs(effective_path)

        response = self.process_response(
            self.kernel_pull_with_http_info(owner_slug, kernel_slug))
        blob = response['blob']

        if os.path.isfile(effective_path):
            effective_dir = os.path.dirname(effective_path)
        else:
            effective_dir = effective_path
        metadata_path = os.path.join(effective_dir, self.KERNEL_METADATA_FILE)

        if not os.path.isfile(effective_path):
            language = blob['language'].lower()
            kernel_type = blob['kernelType'].lower()

            file_name = None
            if existing_metadata:
                file_name = existing_metadata['code_file']
            elif os.path.isfile(metadata_path):
                with open(metadata_path) as f:
                    file_name = json.load(f)['code_file']

            if not file_name or file_name == "INSERT_CODE_FILE_PATH_HERE":
                extension = None
                if kernel_type == 'script':
                    if language == 'python':
                        extension = '.py'
                    elif language == 'r':
                        extension = '.R'
                    elif language == 'rmarkdown':
                        extension = '.Rmd'
                    elif language == 'sqlite':
                        extension = '.sql'
                    elif language == 'julia':
                        extension = '.jl'
                elif kernel_type == 'notebook':
                    if language == 'python':
                        extension = '.ipynb'
                    elif language == 'r':
                        extension = '.irnb'
                    elif language == 'julia':
                        extension = '.ijlnb'
                file_name = blob['slug'] + extension

            if file_name is None:
                print(
                    'Unknown language %s + kernel type %s - please report this '
                    'on the kaggle-api github issues' % (language,
                                                         kernel_type))
                print(
                    'Saving as a python file, even though this may not be the '
                    'correct language')
                file_name = 'script.py'
            script_path = os.path.join(effective_path, file_name)
        else:
            script_path = effective_path
            file_name = os.path.basename(effective_path)

        with open(script_path, 'w') as f:
            f.write(blob['source'])

        if metadata:
            data = {}

            server_metadata = response['metadata']
            data['id'] = server_metadata['ref']
            data['id_no'] = server_metadata['id']
            data['title'] = server_metadata['title']
            data['code_file'] = file_name
            data['language'] = server_metadata['language']
            data['kernel_type'] = server_metadata['kernelType']
            self.set_if_present(server_metadata, 'isPrivate', data,
                                'is_private')
            self.set_if_present(server_metadata, 'enableGpu', data,
                                'enable_gpu')
            self.set_if_present(server_metadata, 'enableInternet', data,
                                'enable_internet')
            self.set_if_present(server_metadata, 'categoryIds', data,
                                'keywords')
            self.set_if_present(server_metadata, 'datasetDataSources', data,
                                'dataset_sources')
            self.set_if_present(server_metadata, 'kernelDataSources', data,
                                'kernel_sources')
            self.set_if_present(server_metadata, 'competitionDataSources',
                                data, 'competition_sources')
            with open(metadata_path, 'w') as f:
                json.dump(data, f, indent=2)

            return effective_dir
        else:
            return script_path