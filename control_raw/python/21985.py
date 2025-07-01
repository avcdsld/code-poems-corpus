def dataset_download_files(self,
                               dataset,
                               path=None,
                               force=False,
                               quiet=True,
                               unzip=False):
        """ download all files for a dataset

            Parameters
            ==========
            dataset: the string identified of the dataset
                     should be in format [owner]/[dataset-name]
            path: the path to download the dataset to
            force: force the download if the file already exists (default False)
            quiet: suppress verbose output (default is True)
            unzip: if True, unzip files upon download (default is False)
        """
        if dataset is None:
            raise ValueError('A dataset must be specified')
        if '/' in dataset:
            self.validate_dataset_string(dataset)
            dataset_urls = dataset.split('/')
            owner_slug = dataset_urls[0]
            dataset_slug = dataset_urls[1]
        else:
            owner_slug = self.get_config_value(self.CONFIG_NAME_USER)
            dataset_slug = dataset

        if path is None:
            effective_path = self.get_default_download_dir(
                'datasets', owner_slug, dataset_slug)
        else:
            effective_path = path

        response = self.process_response(
            self.datasets_download_with_http_info(
                owner_slug=owner_slug,
                dataset_slug=dataset_slug,
                _preload_content=False))

        outfile = os.path.join(effective_path, dataset_slug + '.zip')
        if force or self.download_needed(response, outfile, quiet):
            self.download_file(response, outfile, quiet)
            downloaded = True
        else:
            downloaded = False

        if downloaded:
            outfile = os.path.join(effective_path, dataset_slug + '.zip')
            if unzip:
                try:
                    with zipfile.ZipFile(outfile) as z:
                        z.extractall(effective_path)
                except zipfile.BadZipFile as e:
                    raise ValueError(
                        'Bad zip file, please report on '
                        'www.github.com/kaggle/kaggle-api', e)

                try:
                    os.remove(outfile)
                except OSError as e:
                    print('Could not delete zip file, got %s' % e)