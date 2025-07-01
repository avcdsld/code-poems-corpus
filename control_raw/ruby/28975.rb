def use plugin, *args
      Nutcracker.const_get(plugin.to_s.capitalize).start(self,*args)
    end