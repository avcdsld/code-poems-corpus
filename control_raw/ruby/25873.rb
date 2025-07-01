def console
      client_setup({}, true, true)
      puts "Console Connected to #{@client.url}"
      puts "HINT: The @client object is available to you\n\n"
    rescue
      puts "WARNING: Couldn't connect to #{@options['url'] || ENV['ONEVIEWSDK_URL']}\n\n"
    ensure
      require 'pry'
      Pry.config.prompt = proc { '> ' }
      Pry.plugins['stack_explorer'] && Pry.plugins['stack_explorer'].disable!
      Pry.plugins['byebug'] && Pry.plugins['byebug'].disable!
      Pry.start(OneviewSDK::Console.new(@client))
    end