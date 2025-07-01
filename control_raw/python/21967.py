def competition_submissions(self, competition):
        """ get the list of Submission for a particular competition

            Parameters
            ==========
            competition: the name of the competition
        """
        submissions_result = self.process_response(
            self.competitions_submissions_list_with_http_info(id=competition))
        return [Submission(s) for s in submissions_result]