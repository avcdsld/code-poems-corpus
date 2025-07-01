def load_cookbook(cookbook_name)
        Strainer.ui.debug "Sandbox#load_cookbook('#{cookbook_name.inspect}')"
        cookbook_path = cookbooks_paths.find { |path| path.join(cookbook_name).exist? }

        cookbook = if cookbook_path
          path = cookbook_path.join(cookbook_name)
          Strainer.ui.debug "  found cookbook at '#{path}'"

          begin
            Berkshelf::CachedCookbook.from_path(path)
          rescue Berkshelf::CookbookNotFound
            raise Strainer::Error::CookbookNotFound, "'#{path}' existed, but I could not extract a cookbook. Is there a 'metadata.rb'?"
          end
        else
          Strainer.ui.debug "  did not find '#{cookbook_name}' in any of the sources - resorting to the default cookbook_store..."
          Berkshelf.cookbook_store.cookbooks(cookbook_name).last
        end

        cookbook || raise(Strainer::Error::CookbookNotFound, "Could not find '#{cookbook_name}' in any of the sources.")
      end