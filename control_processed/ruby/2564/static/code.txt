def decrypt_if_necessary(
      zip_file,
      content_entry,
      roo_content_xml_path, options
    )
      # Check if content.xml is encrypted by extracting manifest.xml
      # and searching for a manifest:encryption-data element

      if (manifest_entry = zip_file.glob('META-INF/manifest.xml').first)
        roo_manifest_xml_path = File.join(@tmpdir, 'roo_manifest.xml')
        manifest_entry.extract(roo_manifest_xml_path)
        manifest        = ::Roo::Utils.load_xml(roo_manifest_xml_path)

        # XPath search for manifest:encryption-data only for the content.xml
        # file

        encryption_data = manifest.xpath(
          "//manifest:file-entry[@manifest:full-path='content.xml']"\
        "/manifest:encryption-data"
        ).first

        # If XPath returns a node, then we know content.xml is encrypted

        unless encryption_data.nil?

          # Since we know it's encrypted, we check for the password option
          # and if it doesn't exist, raise an argument error

          password = options[:password]
          if !password.nil?
            perform_decryption(
              encryption_data,
              password,
              content_entry,
              roo_content_xml_path
            )
          else
            fail ArgumentError, 'file is encrypted but password was not supplied'
          end
        end
      else
        fail ArgumentError, 'file missing required META-INF/manifest.xml'
      end
    end