def render_reaction(self, glob_ref, tag, data):
        '''
        Execute the render system against a single reaction file and return
        the data structure
        '''
        react = {}

        if glob_ref.startswith('salt://'):
            glob_ref = self.minion.functions['cp.cache_file'](glob_ref) or ''
        globbed_ref = glob.glob(glob_ref)
        if not globbed_ref:
            log.error('Can not render SLS %s for tag %s. File missing or not found.', glob_ref, tag)
        for fn_ in globbed_ref:
            try:
                res = self.render_template(
                    fn_,
                    tag=tag,
                    data=data)

                # for #20841, inject the sls name here since verify_high()
                # assumes it exists in case there are any errors
                for name in res:
                    res[name]['__sls__'] = fn_

                react.update(res)
            except Exception:
                log.exception('Failed to render "%s": ', fn_)
        return react