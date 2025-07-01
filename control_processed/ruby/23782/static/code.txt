def analyze
      @changes = sort_changes(@changes)
      @changes = @changes.map {|file_path, times_changed| {:file_path => file_path, :times_changed => times_changed }}

      calculate_revision_changes

      @method_changes = sort_changes(@method_changes)
      @method_changes = @method_changes.map {|method, times_changed| {'method' => method, 'times_changed' => times_changed }}
      @class_changes  = sort_changes(@class_changes)
      @class_changes  = @class_changes.map {|klass, times_changed| {'klass' => klass, 'times_changed' => times_changed }}
    end