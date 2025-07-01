def handle_unknown_files(stat)
      if not stat.unknown.empty?
        resp = ChangeFileHelper.ask_how_to_handle_unknown_files(stat)
        if resp == :add
          gitlib.add(stat.unknown)
        end
      end
    end