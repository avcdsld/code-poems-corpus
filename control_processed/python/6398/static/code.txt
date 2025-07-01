def _get_predicted_embedding_addition(self,
                                          checklist_state: ChecklistStatelet,
                                          action_ids: List[int],
                                          action_embeddings: torch.Tensor) -> torch.Tensor:
        """
        Gets the embeddings of desired terminal actions yet to be produced by the decoder, and
        returns their sum for the decoder to add it to the predicted embedding to bias the
        prediction towards missing actions.
        """
        # Our basic approach here will be to figure out which actions we want to bias, by doing
        # some fancy indexing work, then multiply the action embeddings by a mask for those
        # actions, and return the sum of the result.

        # Shape: (num_terminal_actions, 1).  This is 1 if we still want to predict something on the
        # checklist, and 0 otherwise.
        checklist_balance = checklist_state.get_balance().clamp(min=0)

        # (num_terminal_actions, 1)
        actions_in_agenda = checklist_state.terminal_actions
        # (1, num_current_actions)
        action_id_tensor = checklist_balance.new(action_ids).long().unsqueeze(0)
        # Shape: (num_terminal_actions, num_current_actions).  Will have a value of 1 if the
        # terminal action i is our current action j, and a value of 0 otherwise.  Because both sets
        # of actions are free of duplicates, there will be at most one non-zero value per current
        # action, and per terminal action.
        current_agenda_actions = (actions_in_agenda == action_id_tensor).float()

        # Shape: (num_current_actions,).  With the inner multiplication, we remove any current
        # agenda actions that are not in our checklist balance, then we sum over the terminal
        # action dimension, which will have a sum of at most one.  So this will be a 0/1 tensor,
        # where a 1 means to encourage the current action in that position.
        actions_to_encourage = torch.sum(current_agenda_actions * checklist_balance, dim=0)

        # Shape: (action_embedding_dim,).  This is the sum of the action embeddings that we want
        # the model to prefer.
        embedding_addition = torch.sum(action_embeddings * actions_to_encourage.unsqueeze(1),
                                       dim=0,
                                       keepdim=False)

        if self._add_action_bias:
            # If we're adding an action bias, the last dimension of the action embedding is a bias
            # weight.  We don't want this addition to affect the bias (TODO(mattg): or do we?), so
            # we zero out that dimension here.
            embedding_addition[-1] = 0

        return embedding_addition