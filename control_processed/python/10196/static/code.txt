def to_dot(self, f, skip_disconnected=True):
        """Writes a DOT output for the graph to the provided file *f*.

        If *skip_disconnected* is set to ``True``, then all distributions
        that are not dependent on any other distribution are skipped.

        :type f: has to support ``file``-like operations
        :type skip_disconnected: ``bool``
        """
        disconnected = []

        f.write("digraph dependencies {\n")
        for dist, adjs in self.adjacency_list.items():
            if len(adjs) == 0 and not skip_disconnected:
                disconnected.append(dist)
            for other, label in adjs:
                if not label is None:
                    f.write('"%s" -> "%s" [label="%s"]\n' %
                            (dist.name, other.name, label))
                else:
                    f.write('"%s" -> "%s"\n' % (dist.name, other.name))
        if not skip_disconnected and len(disconnected) > 0:
            f.write('subgraph disconnected {\n')
            f.write('label = "Disconnected"\n')
            f.write('bgcolor = red\n')

            for dist in disconnected:
                f.write('"%s"' % dist.name)
                f.write('\n')
            f.write('}\n')
        f.write('}\n')