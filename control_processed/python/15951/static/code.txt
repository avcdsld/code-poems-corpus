def _get_1d_interface_edges(self):
        """
        Get edges that represents transition from not 1D to 1D, and 1D to not 1D
        A 'in_edge e(u,v)' means u operates on non-1D blobs, but v operates on 1D blobs.
        An 'out_edge e(u,v)' means u operates on 1D blobs, but v operates on non-1D blobs.
        """
        in_edges = []
        for layer in self.layer_list:
            if not self.is_1d_layer(layer):
                continue
            preds = self.get_predecessors(layer)
            if len(preds) == 0:
                in_edges.append((None, layer))
            else:
                # because 1D layers are all 1-input, there should only be 1 predecessor
                u, v = preds[0], layer
                while (u != None) and (self.is_activation(u) or type(u) in _KERAS_NORMALIZATION_LAYERS):
                    preds = self.get_predecessors(u)
                    v = u
                    u = preds[0] if len(preds) > 0 else None
                if u is None or (not self.is_1d_layer(u)):
                    in_edges.append((u, v))

        out_edges = []
        for layer in self.layer_list:
            if not self.is_1d_layer(layer):
                continue
            succs = self.get_successors(layer)
            if len(succs) == 0:
                out_edges.append((layer, None))
            elif not self.is_activation(succs[0]):
                for succ in succs:
                    if not self.is_1d_layer(succ):
                        out_edges.append((layer, succ))
            else:
                act_layer = succs[0]
                succs = self.get_successors(act_layer)
                if len(succs) == 0:
                    out_edges.append((act_layer, None))
                else:
                    for succ in succs:
                        if not self.is_1d_layer(succ):
                            out_edges.append((act_layer, succ))

        return in_edges, out_edges