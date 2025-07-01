def _get_rnn_cell(mode, num_layers, input_size, hidden_size,
                  dropout, weight_dropout,
                  var_drop_in, var_drop_state, var_drop_out,
                  skip_connection, proj_size=None, cell_clip=None, proj_clip=None):
    """create rnn cell given specs

    Parameters
    ----------
    mode : str
        The type of RNN cell to use. Options are 'lstmpc', 'rnn_tanh', 'rnn_relu', 'lstm', 'gru'.
    num_layers : int
        The number of RNN cells in the encoder.
    input_size : int
        The initial input size of in the RNN cell.
    hidden_size : int
        The hidden size of the RNN cell.
    dropout : float
        The dropout rate to use for encoder output.
    weight_dropout: float
        The dropout rate to the hidden to hidden connections.
    var_drop_in: float
        The variational dropout rate for inputs. Won’t apply dropout if it equals 0.
    var_drop_state: float
        The variational dropout rate for state inputs on the first state channel.
        Won’t apply dropout if it equals 0.
    var_drop_out: float
        The variational dropout rate for outputs. Won’t apply dropout if it equals 0.
    skip_connection : bool
        Whether to add skip connections (add RNN cell input to output)
    proj_size : int
        The projection size of each LSTMPCellWithClip cell.
        Only available when the mode=lstmpc.
    cell_clip : float
        Clip cell state between [-cellclip, cell_clip] in LSTMPCellWithClip cell.
        Only available when the mode=lstmpc.
    proj_clip : float
        Clip projection between [-projclip, projclip] in LSTMPCellWithClip cell
        Only available when the mode=lstmpc.
    """

    assert mode == 'lstmpc' and proj_size is not None, \
        'proj_size takes effect only when mode is lstmpc'
    assert mode == 'lstmpc' and cell_clip is not None, \
        'cell_clip takes effect only when mode is lstmpc'
    assert mode == 'lstmpc' and proj_clip is not None, \
        'proj_clip takes effect only when mode is lstmpc'

    rnn_cell = rnn.HybridSequentialRNNCell()
    with rnn_cell.name_scope():
        for i in range(num_layers):
            if mode == 'rnn_relu':
                cell = rnn.RNNCell(hidden_size, 'relu', input_size=input_size)
            elif mode == 'rnn_tanh':
                cell = rnn.RNNCell(hidden_size, 'tanh', input_size=input_size)
            elif mode == 'lstm':
                cell = rnn.LSTMCell(hidden_size, input_size=input_size)
            elif mode == 'gru':
                cell = rnn.GRUCell(hidden_size, input_size=input_size)
            elif mode == 'lstmpc':
                cell = LSTMPCellWithClip(hidden_size, proj_size,
                                         cell_clip=cell_clip,
                                         projection_clip=proj_clip,
                                         input_size=input_size)
            if var_drop_in + var_drop_state + var_drop_out != 0:
                cell = contrib.rnn.VariationalDropoutCell(cell,
                                                          var_drop_in,
                                                          var_drop_state,
                                                          var_drop_out)

            if skip_connection:
                cell = rnn.ResidualCell(cell)

            rnn_cell.add(cell)

            if i != num_layers - 1 and dropout != 0:
                rnn_cell.add(rnn.DropoutCell(dropout))

            if weight_dropout:
                apply_weight_drop(rnn_cell, 'h2h_weight', rate=weight_dropout)

    return rnn_cell