def pending_commits
      current_commit = IO.popen("git rev-parse 'HEAD'").read.strip
      format = "%C(yellow)%h%Creset %s %C(red)(%cr)%Creset"
      range = "#{git_info["deployed_commit_sha"]}..#{current_commit}"
      IO.popen(%Q{git log --no-merges --oneline --pretty=format:"#{format}" #{range}}).read.strip
    end