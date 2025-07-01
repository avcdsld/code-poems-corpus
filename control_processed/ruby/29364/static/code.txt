def generate_answers
      the_answers = {}
      masterless  = @options[:masterless]
      database    = masterless ? nil : only_host_with_role(@hosts, 'database')
      dashboard   = masterless ? nil : only_host_with_role(@hosts, 'dashboard')
      master      = masterless ? nil : only_host_with_role(@hosts, 'master')
      @hosts.each do |h|
        if @options[:type] == :upgrade and h[:pe_ver] =~ /\A3.0/
          # 3.0.x to 3.0.x should require no answers
          the_answers[h.name] = {
            :q_install => answer_for(@options, :q_install, 'y'),
            :q_install_vendor_packages => answer_for(@options, :q_install_vendor_packages, 'y'),
          }
        else
          the_answers[h.name] = host_answers(h, master, database, dashboard, @options)
        end
        if the_answers[h.name] && h[:custom_answers]
          the_answers[h.name] = the_answers[h.name].merge(h[:custom_answers])
        end
        h[:answers] = the_answers[h.name]
      end
      return the_answers
    end