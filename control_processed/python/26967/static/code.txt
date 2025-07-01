def rollback(name, **kwargs):
    '''
    Rollbacks the committed changes.

    .. code-block:: yaml

            rollback the changes:
              junos:
                - rollback
                - id: 5

    Parameters:
      Optional
        * id:
          The rollback id value [0-49]. (default = 0)
        * kwargs: Keyworded arguments which can be provided like-
            * timeout:
              Set NETCONF RPC timeout. Can be used for commands which
              take a while to execute. (default = 30 seconds)
            * comment:
              Provide a comment to the commit. (default = None)
            * confirm:
              Provide time in minutes for commit confirmation. If this option \
              is specified, the commit will be rollbacked in the given time \
              unless the commit is confirmed.
            * diffs_file:
              Path to the file where any diffs will be written. (default = None)

    '''
    ret = {'name': name, 'changes': {}, 'result': True, 'comment': ''}
    ret['changes'] = __salt__['junos.rollback'](**kwargs)
    return ret