def merged(revision)
      # By hand, build a list of all branches known to be merged into master
      git_args = ['branch', '-a', '--merged', revision]
      all_merged = []
      @repo.git_output(git_args).lines.each do |line|
        line.strip!
        all_merged << Branch.new(@repo, line)
      end

      # Filter the contents of this collection according to the big list
      merged = []
      @branches.each do |candidate|
        # For some reason Set#include? does not play nice with our overridden comparison operators
        # for branches, so we need to do this the hard way :(
        merged << candidate if all_merged.detect { |b| candidate == b }
      end

      BranchCollection.new(@repo, merged)
    end