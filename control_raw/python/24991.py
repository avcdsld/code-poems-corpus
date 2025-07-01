def recv_chunked(dest, chunk, append=False, compressed=True, mode=None):
    '''
    This function receives files copied to the minion using ``salt-cp`` and is
    not intended to be used directly on the CLI.
    '''
    if 'retcode' not in __context__:
        __context__['retcode'] = 0

    def _error(msg):
        __context__['retcode'] = 1
        return msg

    if chunk is None:
        # dest is an empty dir and needs to be created
        try:
            os.makedirs(dest)
        except OSError as exc:
            if exc.errno == errno.EEXIST:
                if os.path.isfile(dest):
                    return 'Path exists and is a file'
            else:
                return _error(exc.__str__())
        return True

    chunk = base64.b64decode(chunk)

    open_mode = 'ab' if append else 'wb'
    try:
        fh_ = salt.utils.files.fopen(dest, open_mode)  # pylint: disable=W8470
    except (IOError, OSError) as exc:
        if exc.errno != errno.ENOENT:
            # Parent dir does not exist, we need to create it
            return _error(exc.__str__())
        try:
            os.makedirs(os.path.dirname(dest))
        except (IOError, OSError) as makedirs_exc:
            # Failed to make directory
            return _error(makedirs_exc.__str__())
        fh_ = salt.utils.files.fopen(dest, open_mode)  # pylint: disable=W8470

    try:
        # Write the chunk to disk
        fh_.write(salt.utils.gzip_util.uncompress(chunk) if compressed
                  else chunk)
    except (IOError, OSError) as exc:
        # Write failed
        return _error(exc.__str__())
    else:
        # Write successful
        if not append and mode is not None:
            # If this is the first chunk we're writing, set the mode
            #log.debug('Setting mode for %s to %s', dest, oct(mode))
            log.debug('Setting mode for %s to %s', dest, mode)
            try:
                os.chmod(dest, mode)
            except OSError:
                return _error(exc.__str__())
        return True
    finally:
        try:
            fh_.close()
        except AttributeError:
            pass