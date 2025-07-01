def _write_map(self):
        """Called twice during file write. The first populates the values in
        the map with 0s.  The second call writes the final map locations when
        all blocks have been written."""
        if self._map is None:
            self._map = OrderedDict((('stata_data', 0),
                                     ('map', self._file.tell()),
                                     ('variable_types', 0),
                                     ('varnames', 0),
                                     ('sortlist', 0),
                                     ('formats', 0),
                                     ('value_label_names', 0),
                                     ('variable_labels', 0),
                                     ('characteristics', 0),
                                     ('data', 0),
                                     ('strls', 0),
                                     ('value_labels', 0),
                                     ('stata_data_close', 0),
                                     ('end-of-file', 0)))
        # Move to start of map
        self._file.seek(self._map['map'])
        bio = BytesIO()
        for val in self._map.values():
            bio.write(struct.pack(self._byteorder + 'Q', val))
        bio.seek(0)
        self._file.write(self._tag(bio.read(), 'map'))