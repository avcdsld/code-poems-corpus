def process(env)
      @document.zip_contents.to_a.each do |(entry_name, content)|
        @document.current_entry = entry_name
        processors = Template.get_processors(entry_name)
        processors.each { |processor| processor.process(content, env) }
      end
    end