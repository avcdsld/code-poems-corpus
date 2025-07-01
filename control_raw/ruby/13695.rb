def edit(user_name, repo_name, issue_id, params={ })
      _update_user_repo_params(user_name, repo_name)
      _validate_user_repo_params(user, repo) unless user? && repo?
      _validate_presence_of issue_id

      normalize! params
      # _merge_mime_type(:issue, params)
      filter! VALID_ISSUE_PARAM_NAMES, params

      put_request("/1.0/repositories/#{user}/#{repo.downcase}/issues/#{issue_id}/", params)
    end