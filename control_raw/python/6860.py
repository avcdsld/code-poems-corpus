def sample_normalize(self, k_samples=1000, overwrite=False):
        """ Estimate the mean and std of the features from the training set
        Params:
            k_samples (int): Use this number of samples for estimation
        """
        log = logUtil.getlogger()
        log.info("Calculating mean and std from samples")
        # if k_samples is negative then it goes through total dataset
        if k_samples < 0:
            audio_paths = self.audio_paths

        # using sample
        else:
            k_samples = min(k_samples, len(self.train_audio_paths))
            samples = self.rng.sample(self.train_audio_paths, k_samples)
            audio_paths = samples
        manager = Manager()
        return_dict = manager.dict()
        jobs = []
        for threadIndex in range(cpu_count()):
            proc = Process(target=self.preprocess_sample_normalize, args=(threadIndex, audio_paths, overwrite, return_dict))
            jobs.append(proc)
            proc.start()
        for proc in jobs:
            proc.join()

        feat = np.sum(np.vstack([item['feat'] for item in return_dict.values()]), axis=0)
        count = sum([item['count'] for item in return_dict.values()])
        feat_squared = np.sum(np.vstack([item['feat_squared'] for item in return_dict.values()]), axis=0)

        self.feats_mean = feat / float(count)
        self.feats_std = np.sqrt(feat_squared / float(count) - np.square(self.feats_mean))
        np.savetxt(
            generate_file_path(self.save_dir, self.model_name, 'feats_mean'), self.feats_mean)
        np.savetxt(
            generate_file_path(self.save_dir, self.model_name, 'feats_std'), self.feats_std)
        log.info("End calculating mean and std from samples")