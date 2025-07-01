def sort_top_targets(self, top, orders):
        '''
        Returns the sorted high data from the merged top files
        '''
        sorted_top = collections.defaultdict(OrderedDict)
        # pylint: disable=cell-var-from-loop
        for saltenv, targets in six.iteritems(top):
            sorted_targets = sorted(targets,
                    key=lambda target: orders[saltenv][target])
            for target in sorted_targets:
                sorted_top[saltenv][target] = targets[target]
        # pylint: enable=cell-var-from-loop
        return sorted_top