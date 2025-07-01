def set_item(self,item):
        "For inference, will briefly replace the dataset with one that only contains `item`."
        self.item = self.x.process_one(item)
        yield None
        self.item = None