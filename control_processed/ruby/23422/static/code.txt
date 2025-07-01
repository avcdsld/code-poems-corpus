def current_label
      @current_label ||= begin
        API.get("/changes/#{commit.change_id}/detail")["labels"]
          .fetch(GERGICH_REVIEW_LABEL, {})
          .fetch("all", [])
          .select { |label| label["username"] == GERGICH_USER }
          .first
      end
    end