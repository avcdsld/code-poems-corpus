def find_pull_request(base, head, error_if_missing = false)
      logger.info { "Looking for a pull request asking for '#{head}' to be merged into '#{base}' on #{repo}." }

      json = pull_requests
      pr = json.find do |p|
        p[:head][:ref] == head and p[:base][:ref] == base
      end

      raise NotFoundError.new(base, head, repo, json) if error_if_missing && pr.nil?

      pr
    end