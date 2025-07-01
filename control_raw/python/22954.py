def ext_pillar(minion_id, pillar, **kwargs):
    '''
    Obtain the Pillar data from **reclass** for the given ``minion_id``.
    '''

    # If reclass is installed, __virtual__ put it onto the search path, so we
    # don't need to protect against ImportError:
    # pylint: disable=3rd-party-module-not-gated
    from reclass.adapters.salt import ext_pillar as reclass_ext_pillar
    from reclass.errors import ReclassException
    # pylint: enable=3rd-party-module-not-gated

    try:
        # the source path we used above isn't something reclass needs to care
        # about, so filter it:
        filter_out_source_path_option(kwargs)

        # if no inventory_base_uri was specified, initialize it to the first
        # file_roots of class 'base' (if that exists):
        set_inventory_base_uri_default(__opts__, kwargs)

        # I purposely do not pass any of __opts__ or __salt__ or __grains__
        # to reclass, as I consider those to be Salt-internal and reclass
        # should not make any assumptions about it.
        return reclass_ext_pillar(minion_id, pillar, **kwargs)

    except TypeError as e:
        if 'unexpected keyword argument' in six.text_type(e):
            arg = six.text_type(e).split()[-1]
            raise SaltInvocationError('ext_pillar.reclass: unexpected option: '
                                      + arg)
        else:
            raise

    except KeyError as e:
        if 'id' in six.text_type(e):
            raise SaltInvocationError('ext_pillar.reclass: __opts__ does not '
                                      'define minion ID')
        else:
            raise

    except ReclassException as e:
        raise SaltInvocationError('ext_pillar.reclass: {0}'.format(e))