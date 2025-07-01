def wip=(pr)
      label_names = []
      labels.each do |label|
        label_names << label.name
      end
      puts("exist labels:" + label_names.join(", "))
      unless wip?
        begin
          add_label("WIP")
        rescue Octokit::UnprocessableEntity => e
          puts "WIP label is already exists."
          puts e
        end
      end
      github.api.add_labels_to_an_issue(repo, pr, [wip_label])
    end