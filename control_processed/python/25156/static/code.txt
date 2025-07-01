def create_option_group(name, engine_name, major_engine_version,
                        option_group_description, tags=None, region=None,
                        key=None, keyid=None, profile=None):
    '''
    Create an RDS option group

    CLI example to create an RDS option group::

        salt myminion boto_rds.create_option_group my-opt-group mysql 5.6 \
                "group description"
    '''
    res = __salt__['boto_rds.option_group_exists'](name, tags, region, key, keyid,
                                                   profile)
    if res.get('exists'):
        return {'exists': bool(res)}

    try:
        conn = _get_conn(region=region, key=key, keyid=keyid, profile=profile)
        if not conn:
            return {'results': bool(conn)}

        taglist = _tag_doc(tags)
        rds = conn.create_option_group(OptionGroupName=name,
                                       EngineName=engine_name,
                                       MajorEngineVersion=major_engine_version,
                                       OptionGroupDescription=option_group_description,
                                       Tags=taglist)

        return {'exists': bool(rds)}
    except ClientError as e:
        return {'error': __utils__['boto3.get_error'](e)}