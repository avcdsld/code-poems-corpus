def permit! (privilege, options = {})
      return true if Authorization.ignore_access_control
      options = {
        :object => nil,
        :skip_attribute_test => false,
        :context => nil,
        :bang => true
      }.merge(options)
      
      # Make sure we're handling all privileges as symbols.
      privilege = privilege.is_a?( Array ) ?
                  privilege.flatten.collect { |priv| priv.to_sym } :
                  privilege.to_sym
      
      #
      # If the object responds to :proxy_reflection, we're probably working with
      # an association proxy.  Use 'new' to leverage ActiveRecord's builder
      # functionality to obtain an object against which we can check permissions.
      #
      # Example: permit!( :edit, :object => user.posts )
      #
      if Authorization.is_a_association_proxy?(options[:object]) && options[:object].respond_to?(:new)
        options[:object] = (Rails.version < "3.0" ? options[:object] : options[:object].where(nil)).new
      end
      
      options[:context] ||= options[:object] && (
        options[:object].class.respond_to?(:decl_auth_context) ?
            options[:object].class.decl_auth_context :
            options[:object].class.name.tableize.to_sym
      ) rescue NoMethodError
      
      user, roles, privileges = user_roles_privleges_from_options(privilege, options)

      return true if roles.is_a?(Array) and not (roles & omnipotent_roles).empty?

      # find a authorization rule that matches for at least one of the roles and 
      # at least one of the given privileges
      attr_validator = AttributeValidator.new(self, user, options[:object], privilege, options[:context])
      rules = matching_auth_rules(roles, privileges, options[:context])
      
      # Test each rule in turn to see whether any one of them is satisfied.
      rules.each do |rule|
        return true if rule.validate?(attr_validator, options[:skip_attribute_test])
      end

      if options[:bang]
        if rules.empty?
          raise NotAuthorized, "No matching rules found for #{privilege} for #{user.inspect} " +
            "(roles #{roles.inspect}, privileges #{privileges.inspect}, " +
            "context #{options[:context].inspect})."
        else
          raise AttributeAuthorizationError, "#{privilege} not allowed for #{user.inspect} on #{(options[:object] || options[:context]).inspect}."
        end
      else
        false
      end
    end