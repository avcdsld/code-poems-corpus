def del_token(token):
    '''
    Delete an eauth token by name

    CLI Example:

    .. code-block:: shell

        salt-run auth.del_token 6556760736e4077daa601baec2b67c24
    '''
    token_path = os.path.join(__opts__['token_dir'], token)
    if os.path.exists(token_path):
        return os.remove(token_path) is None
    return False