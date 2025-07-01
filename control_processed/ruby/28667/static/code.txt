def remove_groups_from_user(id, group_list = [])
      wf_user_id?(id)
      validate_usergroup_list(group_list)
      api.post([id, 'removeUserGroups'].uri_concat, group_list,
               'application/json')
    end