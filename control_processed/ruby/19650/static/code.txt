def each_task
      return enum_for(__method__) unless block_given?

      @doc.xpath('/nmaprun/taskbegin').each do |task_begin|
        task_end = task_begin.xpath('following-sibling::taskend').first

        yield ScanTask.new(
          task_begin['task'],
          Time.at(task_begin['time'].to_i),
          Time.at(task_end['time'].to_i),
          task_end['extrainfo']
        )
      end

      return self
    end