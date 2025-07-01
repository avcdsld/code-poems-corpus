def _print_summary_map(strm, result_map, ftype):
        """Print summary of certain result map."""
        if len(result_map) == 0:
            return 0
        npass = len([x for k, x in result_map.iteritems() if len(x) == 0])
        strm.write('=====%d/%d %s files passed check=====\n' % (npass, len(result_map), ftype))
        for fname, emap in result_map.iteritems():
            if len(emap) == 0:
                continue
            strm.write('%s: %d Errors of %d Categories map=%s\n' % (
                fname, sum(emap.values()), len(emap), str(emap)))
        return len(result_map) - npass