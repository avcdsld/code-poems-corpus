def cpu
      cpus = []
      procfs_file("stat") do |file|
        file.read.scan(CPU_DATA) do |i, user, nice, system, idle|
          cpus << Cpu.new(i.to_i, user.to_i, system.to_i, nice.to_i, idle.to_i)
        end
      end
      cpus
    end