def setup_common_actions(self):
        """Setup context menu common actions"""
        self.collapse_all_action = create_action(self,
                                     text=_('Collapse all'),
                                     icon=ima.icon('collapse'),
                                     triggered=self.collapseAll)
        self.expand_all_action = create_action(self,
                                     text=_('Expand all'),
                                     icon=ima.icon('expand'),
                                     triggered=self.expandAll)
        self.restore_action = create_action(self,
                                     text=_('Restore'),
                                     tip=_('Restore original tree layout'),
                                     icon=ima.icon('restore'),
                                     triggered=self.restore)
        self.collapse_selection_action = create_action(self,
                                     text=_('Collapse selection'),
                                     icon=ima.icon('collapse_selection'),
                                     triggered=self.collapse_selection)
        self.expand_selection_action = create_action(self,
                                     text=_('Expand selection'),
                                     icon=ima.icon('expand_selection'),
                                     triggered=self.expand_selection)
        return [self.collapse_all_action, self.expand_all_action,
                self.restore_action, None,
                self.collapse_selection_action, self.expand_selection_action]