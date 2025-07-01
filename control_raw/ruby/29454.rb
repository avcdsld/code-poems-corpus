def service_resolved_waiters
      @waiters_mutex.synchronize do
        @waiters.replace(@waiters.to_set - (@working.keys.to_set + solved))
      end

      waiter_iteration = lambda do
        @waiters.each do |group_name|
          if (solved.to_set & vm_dependencies[group_name]).to_a == vm_dependencies[group_name]
            if_debug do
              $stderr.puts "Provisioning #{group_name}"
            end

            provisioner = vm_groups[group_name]

            provision_block = lambda do
              # FIXME maybe a way to specify initial args?
              args = nil
              provisioner.each do |this_prov|
                vm_groups[group_name] = provisioner # force a write to the db
                unless args = this_prov.startup(args)
                  $stderr.puts "Could not provision #{group_name} with provisioner #{this_prov.class.name}"
                  raise "Could not provision #{group_name} with provisioner #{this_prov.class.name}"
                end
              end
              @queue << group_name
            end

            vm_working.add(group_name)

            if @serial
              # HACK: just give the working check something that will always work.
              #       Probably should just mock it.
              @working[group_name] = Thread.new { sleep }
              provision_block.call
            else
              @working[group_name] = Thread.new(&provision_block)
            end
          end
        end
      end

      if @serial
        waiter_iteration.call
      else
        @waiters_mutex.synchronize(&waiter_iteration)
      end
    end