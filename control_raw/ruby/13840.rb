def get_template_roles(signers)
      template_roles = []
      signers.each_with_index do |signer, index|
        template_role = {
          name:     signer[:name],
          email:    signer[:email],
          roleName: signer[:role_name],
          tabs: {
            textTabs:     get_signer_tabs(signer[:text_tabs]),
            checkboxTabs: get_signer_tabs(signer[:checkbox_tabs]),
            numberTabs:   get_signer_tabs(signer[:number_tabs]),
            radioGroupTabs: get_radio_signer_tabs(signer[:radio_group_tabs]),
            fullNameTabs: get_signer_tabs(signer[:fullname_tabs]),
            dateTabs:     get_signer_tabs(signer[:date_tabs])
          }
        }

        if signer[:email_notification]
          template_role[:emailNotification] = signer[:email_notification]
        end

        template_role['clientUserId'] = (signer[:client_id] || signer[:email]).to_s if signer[:embedded] == true
        template_roles << template_role
      end
      template_roles
    end