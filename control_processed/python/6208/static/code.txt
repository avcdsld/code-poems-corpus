def constrained_to(self, initial_sequence: torch.Tensor, keep_beam_details: bool = True) -> 'BeamSearch':
        """
        Return a new BeamSearch instance that's like this one but with the specified constraint.
        """
        return BeamSearch(self._beam_size, self._per_node_beam_size, initial_sequence, keep_beam_details)