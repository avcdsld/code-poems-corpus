def _text(username, password, **kwargs):
    '''
    The text file function can authenticate plaintext and digest methods
    that are available in the :py:func:`hashutil.digest <salt.modules.hashutil.digest>`
    function.
    '''

    filename = kwargs['filename']
    hashtype = kwargs['hashtype']
    field_separator = kwargs['field_separator']
    username_field = kwargs['username_field']-1
    password_field = kwargs['password_field']-1

    with salt.utils.files.fopen(filename, 'r') as pwfile:
        for line in pwfile.readlines():
            fields = line.strip().split(field_separator)

            try:
                this_username = fields[username_field]
            except IndexError:
                log.error('salt.auth.file: username field (%s) does not exist '
                          'in file %s', username_field, filename)
                return False
            try:
                this_password = fields[password_field]
            except IndexError:
                log.error('salt.auth.file: password field (%s) does not exist '
                          'in file %s', password_field, filename)
                return False

            if this_username == username:
                if hashtype == 'plaintext':
                    if this_password == password:
                        return True
                else:
                    # Exceptions for unknown hash types will be raised by hashutil.digest
                    if this_password == __salt__['hashutil.digest'](password, hashtype):
                        return True

                # Short circuit if we've already found the user but the password was wrong
                return False
    return False