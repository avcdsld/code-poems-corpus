def dns scope: nil, retries: nil, timeout: nil
      Google::Cloud.dns @project, @keyfile, scope: scope,
                                            retries: (retries || @retries),
                                            timeout: (timeout || @timeout)
    end