def new(self, item_lists, processor:PreProcessor=None, **kwargs)->'ItemList':
        "Create a new `ItemList` from `items`, keeping the same attributes."
        processor = ifnone(processor, self.processor)
        copy_d = {o:getattr(self,o) for o in self.copy_new}
        kwargs = {**copy_d, **kwargs}
        return self.__class__(item_lists, processor=processor, **kwargs)