def set_todo_results(self, results):
        """Set TODO results and update markers in editor"""
        self.todo_results = results
        self.editor.process_todo(results)