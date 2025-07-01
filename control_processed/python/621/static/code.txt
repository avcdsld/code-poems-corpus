def load_stream(self, stream):
        """
        Deserialize ArrowRecordBatches to an Arrow table and return as a list of pandas.Series.
        """
        batches = super(ArrowStreamPandasSerializer, self).load_stream(stream)
        import pyarrow as pa
        for batch in batches:
            yield [self.arrow_to_pandas(c) for c in pa.Table.from_batches([batch]).itercolumns()]