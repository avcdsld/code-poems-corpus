def check_github_response
      Retriable.retriable(retry_options) do
        yield
      end
    rescue MovedPermanentlyError => e
      fail_with_message(e, "The repository has moved, update your configuration")
    rescue Octokit::Forbidden => e
      fail_with_message(e, "Exceeded retry limit")
    rescue Octokit::Unauthorized => e
      fail_with_message(e, "Error: wrong GitHub token")
    end