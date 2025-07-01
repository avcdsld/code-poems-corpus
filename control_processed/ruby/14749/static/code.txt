def rollback
        super
        each {|transition| transition.machine.write(object, :event, transition.event) unless transition.transient?}
      end