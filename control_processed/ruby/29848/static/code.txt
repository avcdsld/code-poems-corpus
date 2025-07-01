def together
      old = Thread.current.eldritch_group

      group = Group.new
      Thread.current.eldritch_group = group

      yield group

      group.join_all
      Thread.current.eldritch_group = old
    end