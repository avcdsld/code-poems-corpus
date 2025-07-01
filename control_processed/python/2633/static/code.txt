def weight(self, arr:Collection, is_item:bool=True):
        "Bias for item or user (based on `is_item`) for all in `arr`. (Set model to `cpu` and no grad.)"
        idx = self.get_idx(arr, is_item)
        m = self.model
        layer = m.i_weight if is_item else m.u_weight
        return layer(idx)