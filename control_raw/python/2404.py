def new(self, items:Iterator, processor:PreProcessors=None, **kwargs)->'ItemList':
        "Create a new `ItemList` from `items`, keeping the same attributes."
        processor = ifnone(processor, self.processor)
        copy_d = {o:getattr(self,o) for o in self.copy_new}
        kwargs = {**copy_d, **kwargs}
        return self.__class__(items=items, processor=processor, **kwargs)