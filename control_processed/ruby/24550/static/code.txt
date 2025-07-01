def destroy
      return false if interface_type == :bridged

      parent.interface.remove_host_only_network_interface(uuid).wait
      dhcp_server.destroy if dhcp_server(false)

      # Remove from collection
      parent_collection.delete(self, true) if parent_collection

      true
    end