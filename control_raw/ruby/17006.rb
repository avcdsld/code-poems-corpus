def precache_all(output_dir=nil, base_url=nil)
      output_dir ||= File.join(Jammit.public_root, Jammit.package_path)
      cacheable(:js, output_dir).each  {|p| cache(p, 'js',  pack_javascripts(p), output_dir) }
      cacheable(:css, output_dir).each do |p|
        cache(p, 'css', pack_stylesheets(p), output_dir)
        if Jammit.embed_assets
          cache(p, 'css', pack_stylesheets(p, :datauri), output_dir, :datauri)
          if Jammit.mhtml_enabled
            raise MissingConfiguration, "A --base-url option is required in order to generate MHTML." unless base_url
            mtime = latest_mtime package_for(p, :css)[:paths]
            asset_url = "#{base_url}#{Jammit.asset_url(p, :css, :mhtml, mtime)}"
            cache(p, 'css', pack_stylesheets(p, :mhtml, asset_url), output_dir, :mhtml, mtime)
          end
        end
      end
    end