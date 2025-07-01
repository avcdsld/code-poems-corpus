def import_page(path, parent)
      slug = path.split("/").last

      # setting page record
      page =
        if parent.present?
          child = site.pages.where(slug: slug).first_or_initialize
          child.parent = parent
          child
        else
          site.pages.root || site.pages.new(slug: slug)
        end

      content_path = File.join(path, "content.html")

      # If file is newer than page record we'll process it
      if fresh_seed?(page, content_path)

        # reading file content in, resulting in a hash
        fragments_hash  = parse_file_content(content_path)

        # parsing attributes section
        attributes_yaml = fragments_hash.delete("attributes")
        attrs           = YAML.safe_load(attributes_yaml)

        # applying attributes
        layout = site.layouts.find_by(identifier: attrs.delete("layout")) || parent.try(:layout)
        category_ids    = category_names_to_ids(page, attrs.delete("categories"))
        target_page     = attrs.delete("target_page")

        page.attributes = attrs.merge(
          layout: layout,
          category_ids: category_ids
        )

        # applying fragments
        old_frag_identifiers = page.fragments.pluck(:identifier)

        new_frag_identifiers, fragments_attributes =
          construct_fragments_attributes(fragments_hash, page, path)
        page.fragments_attributes = fragments_attributes

        if page.save
          message = "[CMS SEEDS] Imported Page \t #{page.full_path}"
          ComfortableMexicanSofa.logger.info(message)

          # defering target page linking
          if target_page.present?
            self.target_pages ||= {}
            self.target_pages[page.id] = target_page
          end

          # cleaning up old fragments
          page.fragments.where(identifier: old_frag_identifiers - new_frag_identifiers).destroy_all

        else
          message = "[CMS SEEDS] Failed to import Page \n#{page.errors.inspect}"
          ComfortableMexicanSofa.logger.warn(message)
        end
      end

      import_translations(path, page)

      # Tracking what page from seeds we're working with. So we can remove pages
      # that are no longer in seeds
      seed_ids << page.id

      # importing child pages (if there are any)
      Dir["#{path}*/"].each do |page_path|
        import_page(page_path, page)
      end
    end