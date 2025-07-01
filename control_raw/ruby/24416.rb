def revert_to_parent!
      if self.parent
        self.invalidate!
        self.parent.activate!
        self.parent.controller = self.controller
        self.parent.set_cookie!
        self.parent
      else
        raise NoParentSessionForRevert, "Session does not have a parent therefore cannot be reverted."
      end
    end