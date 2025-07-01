def build_us_rate_request(packages, origin_zip, destination_zip, options = {})
      xml_builder = Nokogiri::XML::Builder.new do |xml|
        xml.RateV4Request('USERID' => @options[:login]) do
          Array(packages).each_with_index do |package, id|
            xml.Package('ID' => id) do
              commercial_type = commercial_type(options)
              default_service = DEFAULT_SERVICE[commercial_type]
              service         = options.fetch(:service, default_service).to_sym

              if commercial_type && service != default_service
                raise ArgumentError, "Commercial #{commercial_type} rates are only provided with the #{default_service.inspect} service."
              end

              xml.Service(US_SERVICES[service])
              xml.FirstClassMailType(FIRST_CLASS_MAIL_TYPES[options[:first_class_mail_type].try(:to_sym)])
              xml.ZipOrigination(strip_zip(origin_zip))
              xml.ZipDestination(strip_zip(destination_zip))
              xml.Pounds(0)
              xml.Ounces("%0.1f" % [package.ounces, 1].max)
              size_code = USPS.size_code_for(package)
              container = CONTAINERS[package.options[:container]]
              container ||= (package.cylinder? ? 'NONRECTANGULAR' : 'RECTANGULAR') if size_code == 'LARGE'
              xml.Container(container)
              xml.Size(size_code)
              xml.Width("%0.2f" % package.inches(:width))
              xml.Length("%0.2f" % package.inches(:length))
              xml.Height("%0.2f" % package.inches(:height))
              xml.Girth("%0.2f" % package.inches(:girth))
              is_machinable = if package.options.has_key?(:machinable)
                package.options[:machinable] ? true : false
              else
                USPS.package_machinable?(package)
              end
              xml.Machinable(is_machinable.to_s.upcase)
            end
          end
        end
      end
      save_request(xml_builder.to_xml)
    end