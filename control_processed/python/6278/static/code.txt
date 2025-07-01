def count_vocab_items(self, counter: Dict[str, Dict[str, int]]):
        """
        Increments counts in the given ``counter`` for all of the vocabulary items in all of the
        ``Fields`` in this ``Instance``.
        """
        for field in self.fields.values():
            field.count_vocab_items(counter)