def prune_dead_workers
      all_workers = self.class.all
      return if all_workers.empty?
      known_workers = JRUBY ? worker_thread_ids : []
      pids = nil, hostname = self.hostname
      all_workers.each do |worker|
        host, pid, thread, queues = self.class.split_id(worker.id)
        next if host != hostname
        next if known_workers.include?(thread) && pid == self.pid.to_s
        # NOTE: allow flexibility of running workers :
        # 1. worker might run in another JVM instance
        # 2. worker might run as a process (with MRI)
        next if (pids ||= system_pids).include?(pid)
        log! "Pruning dead worker: #{worker}"
        if worker.respond_to?(:unregister_worker)
          worker.unregister_worker
        else # Resque 2.x
          Registry.for(worker).unregister
        end
      end
    end