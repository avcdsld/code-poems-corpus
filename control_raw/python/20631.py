def post_copy_metacolums(self, cursor):
        """
        Performs post-copy to fill metadata columns.
        """
        logger.info('Executing post copy metadata queries')
        for query in self.metadata_queries:
            cursor.execute(query)