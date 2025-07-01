def create(embedding_name, **kwargs):
    """Creates an instance of token embedding.


    Creates a token embedding instance by loading embedding vectors from an externally hosted
    pre-trained token embedding file, such as those of GloVe and FastText. To get all the valid
    `embedding_name` and `pretrained_file_name`, use
    `mxnet.contrib.text.embedding.get_pretrained_file_names()`.


    Parameters
    ----------
    embedding_name : str
        The token embedding name (case-insensitive).


    Returns
    -------
    An instance of `mxnet.contrib.text.glossary._TokenEmbedding`:
        A token embedding instance that loads embedding vectors from an externally hosted
        pre-trained token embedding file.
    """

    create_text_embedding = registry.get_create_func(_TokenEmbedding, 'token embedding')
    return create_text_embedding(embedding_name, **kwargs)