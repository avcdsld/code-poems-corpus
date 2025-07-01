def clone_from(self, other):
        """Clone EditorStack from other instance"""
        for other_finfo in other.data:
            self.clone_editor_from(other_finfo, set_current=True)
        self.set_stack_index(other.get_stack_index())