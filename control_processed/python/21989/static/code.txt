def dataset_create_version_cli(self,
                                   folder,
                                   version_notes,
                                   quiet=False,
                                   convert_to_csv=True,
                                   delete_old_versions=False,
                                   dir_mode='skip'):
        """ client wrapper for creating a version of a dataset
             Parameters
            ==========
            folder: the folder with the dataset configuration / data files
            version_notes: notes to add for the version
            quiet: suppress verbose output (default is False)
            convert_to_csv: on upload, if data should be converted to csv
            delete_old_versions: if True, do that (default False)
            dir_mode: What to do with directories: "skip" - ignore; "zip" - compress and upload
        """
        folder = folder or os.getcwd()
        result = self.dataset_create_version(
            folder,
            version_notes,
            quiet=quiet,
            convert_to_csv=convert_to_csv,
            delete_old_versions=delete_old_versions,
            dir_mode=dir_mode)
        if result.invalidTags:
            print(
                ('The following are not valid tags and could not be added to '
                 'the dataset: ') + str(result.invalidTags))
        if result is None:
            print('Dataset version creation error: See previous output')
        elif result.status.lower() == 'ok':
            print('Dataset version is being created. Please check progress at '
                  + result.url)
        else:
            print('Dataset version creation error: ' + result.error)