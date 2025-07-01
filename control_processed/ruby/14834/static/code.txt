def try_process_smashed_arg(flag)
      option = matching_option(flag[0, 2])
      if option && option.expects_argument?
        process(option, flag[2..-1])
      end
    end