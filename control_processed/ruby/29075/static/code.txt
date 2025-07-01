def find(handle)
      handle = Entity::Handle.build(:number => handle) unless handle.is_a?(Entity::Handle)
      super(handle)
    end