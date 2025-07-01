def init_remote(self):
        '''
        Initialize/attach to a remote using GitPython. Return a boolean
        which will let the calling function know whether or not a new repo was
        initialized by this function.
        '''
        new = False
        if not os.listdir(self.cachedir):
            # Repo cachedir is empty, initialize a new repo there
            self.repo = git.Repo.init(self.cachedir)
            new = True
        else:
            # Repo cachedir exists, try to attach
            try:
                self.repo = git.Repo(self.cachedir)
            except git.exc.InvalidGitRepositoryError:
                log.error(_INVALID_REPO, self.cachedir, self.url, self.role)
                return new

        self.gitdir = salt.utils.path.join(self.repo.working_dir, '.git')
        self.enforce_git_config()

        return new