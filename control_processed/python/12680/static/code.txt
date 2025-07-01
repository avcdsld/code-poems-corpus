def get_variable(name, temp_s):
    '''
    Get variable by name.
    '''
    return tf.Variable(tf.zeros(temp_s), name=name)