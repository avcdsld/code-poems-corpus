def load_thread_for_message m, opts={}
    good = @index.each_message_in_thread_for m, opts do |mid, builder|
      next if contains_id? mid
      add_message builder.call
    end
    add_message m if good
  end