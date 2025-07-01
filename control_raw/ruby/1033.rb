def invitation_instructions(user, token, opts = {})
      with_user(user) do
        @token = token
        @organization = user.organization
        @opts = opts

        opts[:subject] = I18n.t("devise.mailer.#{opts[:invitation_instructions]}.subject", organization: user.organization.name) if opts[:invitation_instructions]
      end

      devise_mail(user, opts[:invitation_instructions] || :invitation_instructions, opts)
    end