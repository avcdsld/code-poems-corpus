def exit_if_failures!(resp)
      return if resp[:failures].nil? || resp[:failures].empty?

      puts "There was a failure running the ECS task.".color(:red)
      puts "This might be happen if you have a network_mode of awsvpc and have assigned_public_ip to DISABLED."
      puts "This cryptic error also shows up if the network settings have security groups and subnets that are not in the same vpc as the ECS cluster container instances.  Please double check that."
      puts "You can use this command to quickly reconfigure the network settings:"
      puts "  ufo network init --vpc-id XXX."
      puts "More details on the can be found under the 'Task Networking Considerations' section at: "
      puts "https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-networking.html"
      puts "Original response with failures:"
      pp resp
      exit 1
    end