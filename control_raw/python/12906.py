def get_main_chain_layers(self):
        """Return a list of layer IDs in the main chain."""
        main_chain = self.get_main_chain()
        ret = []
        for u in main_chain:
            for v, layer_id in self.adj_list[u]:
                if v in main_chain and u in main_chain:
                    ret.append(layer_id)
        return ret