def whats_next
      say ''
      say 'All done!', :green

      say ''
      say "I've added a few things here and there to set you up using Vue in your Rails app."
      say "Now you're already to create your first Vue component in app/components."
      say ''

      say 'To run the webpack-dev-server and rails server:'
      say 'foreman start -f Procfile.dev', :yellow
      say ''

      say 'For more info, see the README.md for this gem at:'
      say 'https://github.com/samtgarson/vueport', :blue
      say ''

      say 'Thanks for using Vueport!'
    end