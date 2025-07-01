def flush(self, table):
        '''
        Flush table.

        :param table:
        :return:
        '''
        table_path = os.path.join(self.db_path, table)
        if os.path.exists(table_path):
            os.unlink(table_path)