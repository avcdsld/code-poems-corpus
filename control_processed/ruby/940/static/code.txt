def scopes_picker_field(form, name, root: false, options: { checkboxes_on_top: true })
      root = current_participatory_space.scope if root == false
      form.scopes_picker name, options do |scope|
        { url: decidim.scopes_picker_path(root: root, current: scope&.id, field: form.label_for(name)),
          text: scope_name_for_picker(scope, I18n.t("decidim.scopes.global")) }
      end
    end