def run_job(rdd, f, partitions=nil, allow_local=false)
      run_job_with_command(rdd, partitions, allow_local, Spark::Command::MapPartitions, f)
    end