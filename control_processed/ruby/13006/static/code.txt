def multi_toggle_spam threads
    undos = threads.map { |t| actually_toggle_spammed t }
    threads.each { |t| HookManager.run("mark-as-spam", :thread => t) }
    UndoManager.register "marking/unmarking  #{threads.size.pluralize 'thread'} as spam",
                         undos, lambda { regen_text }, lambda { threads.each { |t| Index.save_thread t } }
    regen_text
    threads.each { |t| Index.save_thread t }
  end