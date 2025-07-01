def new_from_plist(uuid, objects_by_uuid_plist, root_object = false)
      attributes = objects_by_uuid_plist[uuid]
      if attributes
        klass = Object.const_get(attributes['isa'])
        object = klass.new(self, uuid)
        objects_by_uuid[uuid] = object
        object.add_referrer(self) if root_object
        object.configure_with_plist(objects_by_uuid_plist)
        object
      end
    end