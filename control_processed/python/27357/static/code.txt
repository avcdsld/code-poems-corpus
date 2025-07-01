def purge(self, dbid):
        '''
        Purge the database.

        :param dbid:
        :return:
        '''
        db_path = os.path.join(self.path, dbid)
        if os.path.exists(db_path):
            shutil.rmtree(db_path, ignore_errors=True)
            return True
        return False