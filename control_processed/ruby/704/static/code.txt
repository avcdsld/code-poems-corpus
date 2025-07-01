def process_configured_plugins
      return if !Vagrant.plugins_enabled?
      errors = vagrantfile.config.vagrant.validate(nil)
      if !errors["vagrant"].empty?
        raise Errors::ConfigInvalid,
          errors: Util::TemplateRenderer.render(
            "config/validation_failed",
            errors: errors)
      end
      # Check if defined plugins are installed
      installed = Plugin::Manager.instance.installed_plugins
      needs_install = []
      config_plugins = vagrantfile.config.vagrant.plugins
      config_plugins.each do |name, info|
        if !installed[name]
          needs_install << name
        end
      end
      if !needs_install.empty?
        ui.warn(I18n.t("vagrant.plugins.local.uninstalled_plugins",
          plugins: needs_install.sort.join(", ")))
        if !Vagrant.auto_install_local_plugins?
          answer = nil
          until ["y", "n"].include?(answer)
            answer = ui.ask(I18n.t("vagrant.plugins.local.request_plugin_install") + " [N]: ")
            answer = answer.strip.downcase
            answer = "n" if answer.to_s.empty?
          end
          if answer == "n"
            raise Errors::PluginMissingLocalError,
              plugins: needs_install.sort.join(", ")
          end
        end
        needs_install.each do |name|
          pconfig = Util::HashWithIndifferentAccess.new(config_plugins[name])
          ui.info(I18n.t("vagrant.commands.plugin.installing", name: name))

          options = {sources: Vagrant::Bundler::DEFAULT_GEM_SOURCES.dup, env_local: true}
          options[:sources] = pconfig[:sources] if pconfig[:sources]
          options[:require] = pconfig[:entry_point] if pconfig[:entry_point]
          options[:version] = pconfig[:version] if pconfig[:version]

          spec = Plugin::Manager.instance.install_plugin(name, options)

          ui.info(I18n.t("vagrant.commands.plugin.installed",
            name: spec.name, version: spec.version.to_s))
        end
        ui.info("\n")
        # Force halt after installation and require command to be run again. This
        # will proper load any new locally installed plugins which are now available.
        ui.warn(I18n.t("vagrant.plugins.local.install_rerun_command"))
        exit(-1)
      end
      Vagrant::Plugin::Manager.instance.local_file.installed_plugins
    end