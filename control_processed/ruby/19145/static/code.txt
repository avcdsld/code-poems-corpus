def user_agent_excluded?
      request.user_agent.to_s.downcase =~ Regexp.union([self.mobylette_options[:skip_user_agents]].flatten.map(&:to_s))
    end