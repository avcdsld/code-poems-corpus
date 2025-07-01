def render_crumbs(crumbs, options = {})

      options[:skip_if_blank] ||= Crummy.configuration.skip_if_blank
      return '' if options[:skip_if_blank] && crumbs.count < 1
      options[:format] ||= Crummy.configuration.format
      options[:separator] ||= Crummy.configuration.send(:"#{options[:format]}_separator")
      options[:right_separator] ||= Crummy.configuration.send(:"#{options[:format]}_right_separator")
      options[:links] ||= Crummy.configuration.links
      options[:first_class] ||= Crummy.configuration.first_class
      options[:last_class] ||= Crummy.configuration.last_class
      options[:microdata] ||= Crummy.configuration.microdata if options[:microdata].nil?
      options[:truncate] ||= Crummy.configuration.truncate if options[:truncate]
      options[:last_crumb_linked] = Crummy.configuration.last_crumb_linked if options[:last_crumb_linked].nil?
      options[:right_side] ||= Crummy.configuration.right_side

      last_hash = lambda {|o|k=o.map{|c|
                                      c.is_a?(Hash) ? (c.empty? ? nil: c) : nil}.compact
                                      k.empty? ? {} : k.last
                                    }
      local_global = lambda {|crumb, global_options, param_name| last_hash.call(crumb).has_key?(param_name.to_sym) ? last_hash.call(crumb)[param_name.to_sym] : global_options[param_name.to_sym]}

      case options[:format]
      when :html
        crumb_string = crumbs.map{|crumb|local_global.call(crumb, options, :right_side) ? nil :
                        crumb_to_html(crumb,
                                      local_global.call(crumb, options, :links),
                                      local_global.call(crumb, options, :first_class),
                                      local_global.call(crumb, options, :last_class),
                                      (crumb == crumbs.first),
                                      (crumb == crumbs.last),
                                      local_global.call(crumb, options, :microdata),
                                      local_global.call(crumb, options, :last_crumb_linked),
                                      local_global.call(crumb, options, :truncate))}.compact.join(options[:separator]).html_safe
        crumb_string
      when :html_list
        # Let's set values for special options of html_list format
        options[:li_class] ||= Crummy.configuration.li_class
        options[:ol_class] ||= Crummy.configuration.ol_class
        options[:ol_id] ||= Crummy.configuration.ol_id
        options[:ol_id] = nil if options[:ol_id].blank?

        crumb_string = crumbs.map{|crumb|local_global.call(crumb, options, :right_side) ? nil :
                        crumb_to_html_list(crumb,
                                           local_global.call(crumb, options, :links),
                                           local_global.call(crumb, options, :li_class),
                                           local_global.call(crumb, options, :first_class),
                                           local_global.call(crumb, options, :last_class),
                                           (crumb == crumbs.first),
                                           (crumb == crumbs.find_all{|crumb|
                                                    !last_hash.call(crumb).fetch(:right_side,false)}.compact.last),
                                           local_global.call(crumb, options, :microdata),
                                           local_global.call(crumb, options, :last_crumb_linked),
                                           local_global.call(crumb, options, :truncate),
                                           local_global.call(crumb, options, :separator))}.compact.join.html_safe
        crumb_right_string = crumbs.reverse.map{|crumb|!local_global.call(crumb, options, :right_side) ? nil :

                        crumb_to_html_list(crumb,
                                           local_global.call(crumb, options, :links),
                                           local_global.call(crumb, options, :li_right_class),
                                           local_global.call(crumb, options, :first_class),
                                           local_global.call(crumb, options, :last_class),
                                           (crumb == crumbs.first),
                                           (crumb == crumbs.find_all{|crumb|!local_global.call(crumb, options, :right_side)}.compact.last),
                                           local_global.call(crumb, options, :microdata),
                                           local_global.call(crumb, options, :last_crumb_linked),
                                           local_global.call(crumb, options, :truncate),
                                           local_global.call(crumb, options, :right_separator))}.compact.join.html_safe
        crumb_string = content_tag(:ol,
                                   crumb_string+crumb_right_string,
                                   :class => options[:ol_class],
                                   :id => options[:ol_id])
        crumb_string
      when :xml
        crumbs.collect do |crumb|
          crumb_to_xml(crumb,
                      local_global.call(crumb, options, :links),
                      local_global.call(crumb, options, :separator),
                      (crumb == crumbs.first),
                      (crumb == crumbs.last))
        end * ''
      else
        raise ArgumentError, "Unknown breadcrumb output format"
      end
    end