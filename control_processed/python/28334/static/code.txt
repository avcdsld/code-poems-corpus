def set_volumes_tags(tag_maps, authoritative=False, dry_run=False,
                    region=None, key=None, keyid=None, profile=None):
    '''
    .. versionadded:: 2016.11.0

    tag_maps (list)
        List of dicts of filters and tags, where 'filters' is a dict suitable for passing to the
        'filters' argument of get_all_volumes() above, and 'tags' is a dict of tags to be set on
        volumes (via create_tags/delete_tags) as matched by the given filters.  The filter syntax
        is extended to permit passing either a list of volume_ids or an instance_name (with
        instance_name being the Name tag of the instance to which the desired volumes are mapped).
        Each mapping in the list is applied separately, so multiple sets of volumes can be all
        tagged differently with one call to this function.  If filtering by instance Name, You may
        additionally limit the instances matched by passing in a list of desired instance states.
        The default set of states is ('pending', 'rebooting', 'running', 'stopping', 'stopped').

    YAML example fragment:

    .. code-block:: yaml

        - filters:
            attachment.instance_id: i-abcdef12
          tags:
            Name: dev-int-abcdef12.aws-foo.com
        - filters:
            attachment.device: /dev/sdf
          tags:
            ManagedSnapshots: true
            BillingGroup: bubba.hotep@aws-foo.com
          in_states:
          - stopped
          - terminated
        - filters:
            instance_name: prd-foo-01.aws-foo.com
          tags:
            Name: prd-foo-01.aws-foo.com
            BillingGroup: infra-team@aws-foo.com
        - filters:
            volume_ids: [ vol-12345689, vol-abcdef12 ]
          tags:
            BillingGroup: infra-team@aws-foo.com

    authoritative (bool)
        If true, any existing tags on the matched volumes, and not explicitly requested here, will
        be removed.

    dry_run (bool)
        If true, don't change anything, just return a dictionary describing any changes which
        would have been applied.

    returns (dict)
        A dict describing status and any changes.

    '''
    ret = {'success': True, 'comment': '', 'changes': {}}
    running_states = ('pending', 'rebooting', 'running', 'stopping', 'stopped')
    ### First creeate a dictionary mapping all changes for a given volume to it's volume ID...
    tag_sets = {}
    for tm in tag_maps:
        filters = dict(tm.get('filters', {}))
        tags = dict(tm.get('tags', {}))
        args = {'return_objs': True, 'region': region, 'key': key, 'keyid': keyid, 'profile': profile}
        new_filters = {}
        log.debug('got filters: %s', filters)
        instance_id = None
        in_states = tm.get('in_states', running_states)
        try:
            for k, v in filters.items():
                if k == 'volume_ids':
                    args['volume_ids'] = v
                elif k == 'instance_name':
                    instance_id = get_id(name=v, in_states=in_states, region=region, key=key,
                                         keyid=keyid, profile=profile)
                    if not instance_id:
                        msg = "Couldn't resolve instance Name {0} to an ID.".format(v)
                        raise CommandExecutionError(msg)
                    new_filters['attachment.instance_id'] = instance_id
                else:
                    new_filters[k] = v
        except CommandExecutionError as e:
            log.warning(e)
            continue  # Hmme, abort or do what we can...?  Guess the latter for now.
        args['filters'] = new_filters
        volumes = get_all_volumes(**args)
        log.debug('got volume list: %s', volumes)
        for vol in volumes:
            tag_sets.setdefault(vol.id.replace('-', '_'), {'vol': vol, 'tags': tags.copy()})['tags'].update(tags.copy())
    log.debug('tag_sets after munging: %s', tag_sets)

    ### ...then loop through all those volume->tag pairs and apply them.
    changes = {'old': {}, 'new': {}}
    for volume in tag_sets.values():
        vol, tags = volume['vol'], volume['tags']
        log.debug('current tags on vol.id %s: %s', vol.id, dict(getattr(vol, 'tags', {})))
        curr = set(dict(getattr(vol, 'tags', {})).keys())
        log.debug('requested tags on vol.id %s: %s', vol.id, tags)
        req = set(tags.keys())
        add = list(req - curr)
        update = [r for r in (req & curr) if vol.tags[r] != tags[r]]
        remove = list(curr - req)
        if add or update or (authoritative and remove):
            changes['old'][vol.id] = dict(getattr(vol, 'tags', {}))
            changes['new'][vol.id] = tags
        else:
            log.debug('No changes needed for vol.id %s', vol.id)
        if add:
            d = dict((k, tags[k]) for k in add)
            log.debug('New tags for vol.id %s: %s', vol.id, d)
        if update:
            d = dict((k, tags[k]) for k in update)
            log.debug('Updated tags for vol.id %s: %s', vol.id, d)
        if not dry_run:
            if not create_tags(vol.id, tags, region=region, key=key, keyid=keyid, profile=profile):
                ret['success'] = False
                ret['comment'] = "Failed to set tags on vol.id {0}: {1}".format(vol.id, tags)
                return ret
            if authoritative:
                if remove:
                    log.debug('Removed tags for vol.id %s: %s', vol.id, remove)
                    if not delete_tags(vol.id, remove, region=region, key=key, keyid=keyid, profile=profile):
                        ret['success'] = False
                        ret['comment'] = "Failed to remove tags on vol.id {0}: {1}".format(vol.id, remove)
                        return ret
    ret['changes'].update(changes) if changes['old'] or changes['new'] else None  # pylint: disable=W0106
    return ret