def self_relationship
      @self_relationship ||=
        begin
          model = self.model
          Associations::OneToMany::Relationship.new(
            :self,
            model,
            model,
            self_relationship_options
          )
        end
    end