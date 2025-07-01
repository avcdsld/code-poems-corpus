def calculate_mean_edit_distance_and_loss(iterator, dropout, reuse):
    r'''
    This routine beam search decodes a mini-batch and calculates the loss and mean edit distance.
    Next to total and average loss it returns the mean edit distance,
    the decoded result and the batch's original Y.
    '''
    # Obtain the next batch of data
    (batch_x, batch_seq_len), batch_y = iterator.get_next()

    # Calculate the logits of the batch
    logits, _ = create_model(batch_x, batch_seq_len, dropout, reuse=reuse)

    # Compute the CTC loss using TensorFlow's `ctc_loss`
    total_loss = tf.nn.ctc_loss(labels=batch_y, inputs=logits, sequence_length=batch_seq_len)

    # Calculate the average loss across the batch
    avg_loss = tf.reduce_mean(total_loss)

    # Finally we return the average loss
    return avg_loss