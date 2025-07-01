def active_admin_import(options = {}, &block)
      options.assert_valid_keys(*Options::VALID_OPTIONS)

      options = Options.options_for(config, options)
      params_key = ActiveModel::Naming.param_key(options[:template_object])

      collection_action :import, method: :get do
        authorize!(ActiveAdminImport::Auth::IMPORT, active_admin_config.resource_class)
        @active_admin_import_model = options[:template_object]
        render template: options[:template]
      end

      action_item :import, only: :index, if: options[:if] do
        if authorized?(ActiveAdminImport::Auth::IMPORT, active_admin_config.resource_class)
          link_to(
            I18n.t('active_admin_import.import_model', plural_model: options[:plural_resource_label]),
            action: :import
          )
        end
      end

      collection_action :do_import, method: :post do
        authorize!(ActiveAdminImport::Auth::IMPORT, active_admin_config.resource_class)
        _params = params.respond_to?(:to_unsafe_h) ? params.to_unsafe_h : params
        params = ActiveSupport::HashWithIndifferentAccess.new _params
        @active_admin_import_model = options[:template_object]
        @active_admin_import_model.assign_attributes(params[params_key].try(:deep_symbolize_keys) || {})
        # go back to form
        return render template: options[:template] unless @active_admin_import_model.valid?
        @importer = Importer.new(
          options[:resource_class],
          @active_admin_import_model,
          options
        )
        begin
          result = @importer.import

          if block_given?
            instance_eval(&block)
          else
            instance_exec result, options, &DEFAULT_RESULT_PROC
          end
        rescue ActiveRecord::Import::MissingColumnError, NoMethodError, ActiveRecord::StatementInvalid, CSV::MalformedCSVError => e
          Rails.logger.error(I18n.t('active_admin_import.file_error', message: e.message))
          Rails.logger.error(e.backtrace.join("\n"))
          flash[:error] = I18n.t('active_admin_import.file_error', message: e.message[0..200])
        end
        redirect_to options[:back]
      end
      # rubocop:enable Metrics/AbcSize
    end