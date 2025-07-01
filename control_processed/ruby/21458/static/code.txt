def check_out_branch
      git.check_out branch_to_merge_into
    rescue Git::NoBranchOfType
      cli.say "No #{branch_type} branch available. Creating one now."
      git.check_out DatedBranchCreator.perform(branch_type).branch_name
    end