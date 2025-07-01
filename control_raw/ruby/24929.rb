def entry_xml(title = '', content = '', categories = [], draft = 'no', updated = '', author_name = @user_id)
      builder = Nokogiri::XML::Builder.new(encoding: 'utf-8') do |xml|
        xml.entry('xmlns'     => 'http://www.w3.org/2005/Atom',
                  'xmlns:app' => 'http://www.w3.org/2007/app') do
          xml.title title
          xml.author do
            xml.name author_name
          end
          xml.content(content, type: 'text/x-markdown')
          xml.updated updated unless updated.empty? || updated.nil?
          categories.each do |category|
            xml.category(term: category)
          end
          xml['app'].control do
            xml['app'].draft draft
          end
        end
      end

      builder.to_xml
    end