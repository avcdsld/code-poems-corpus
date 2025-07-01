def enable_root(host)
      if host['user'] != 'root'
        if host['platform'] =~ /f5-/
          enable_root_f5(host)
        elsif host['platform'] =~ /netscaler/
          enable_root_netscaler(host)
        else
          copy_ssh_to_root(host, @options)
          enable_root_login(host, @options)
          host['user'] = 'root'
        end
        host.close
      end
    end