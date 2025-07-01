def filterAcceptsRow(self, row, parent_index):
        """Reimplement Qt method"""
        if self.root_path is None:
            return True
        index = self.sourceModel().index(row, 0, parent_index)
        path = osp.normcase(osp.normpath(
            to_text_string(self.sourceModel().filePath(index))))
        if osp.normcase(self.root_path).startswith(path):
            # This is necessary because parent folders need to be scanned
            return True
        else:
            for p in [osp.normcase(p) for p in self.path_list]:
                if path == p or path.startswith(p+os.sep):
                    return True
            else:
                return False