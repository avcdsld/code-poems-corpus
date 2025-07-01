def parent(self):
        """
        Return the parent scope.

        :return: FoldScope or None
        """
        if TextBlockHelper.get_fold_lvl(self._trigger) > 0 and \
                self._trigger.blockNumber():
            block = self._trigger.previous()
            ref_lvl = self.trigger_level - 1
            while (block.blockNumber() and
                    (not TextBlockHelper.is_fold_trigger(block) or
                     TextBlockHelper.get_fold_lvl(block) > ref_lvl)):
                block = block.previous()
            try:
                return FoldScope(block)
            except ValueError:
                return None
        return None