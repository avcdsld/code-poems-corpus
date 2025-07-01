def data(self, index, role=Qt.DisplayRole):
        """Return a model data element"""
        if not index.isValid():
            return to_qvariant()
        if role == Qt.DisplayRole:
            return self._display_data(index)
        elif role == Qt.BackgroundColorRole:
            return to_qvariant(get_color(self._data[index.row()][index.column()], .2))
        elif role == Qt.TextAlignmentRole:
            return to_qvariant(int(Qt.AlignRight|Qt.AlignVCenter))
        return to_qvariant()