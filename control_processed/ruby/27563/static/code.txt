def set_default_configuration
      ActiveSupport::Deprecation.warn("The environment variable RAILS_DATAROOT will be deprecated in an upcoming release, please use OOD_DATAROOT instead.") if ENV['RAILS_DATAROOT']
      self.dataroot = ENV['OOD_DATAROOT'] || ENV['RAILS_DATAROOT']
      self.dataroot ||= "~/#{ENV['OOD_PORTAL'] || "ondemand"}/data/#{ENV['APP_TOKEN']}" if ENV['APP_TOKEN']

      # Add markdown template support
      self.markdown = Redcarpet::Markdown.new(
        Redcarpet::Render::HTML,
        autolink: true,
        tables: true,
        strikethrough: true,
        fenced_code_blocks: true,
        no_intra_emphasis: true
      )

      # Initialize URL handlers for system apps
      self.public    = Urls::Public.new(
        title:    ENV['OOD_PUBLIC_TITLE'] || 'Public Assets',
        base_url: ENV['OOD_PUBLIC_URL']   || '/public'
      )
      self.dashboard = Urls::Dashboard.new(
        title:    ENV['OOD_DASHBOARD_TITLE'] || 'Open OnDemand',
        base_url: ENV['OOD_DASHBOARD_URL']   || '/pun/sys/dashboard'
      )
      self.shell     = Urls::Shell.new(
        title:    ENV['OOD_SHELL_TITLE'] || 'Shell',
        base_url: ENV['OOD_SHELL_URL']   || '/pun/sys/shell'
      )
      self.files     = Urls::Files.new(
        title:    ENV['OOD_FILES_TITLE'] || 'Files',
        base_url: ENV['OOD_FILES_URL']   || '/pun/sys/files'
      )
      self.editor    = Urls::Editor.new(
        title:    ENV['OOD_EDITOR_TITLE'] || 'Editor',
        base_url: ENV['OOD_EDITOR_URL']   || '/pun/sys/file-editor'
      )

      # Add routes for useful features
      self.routes = OpenStruct.new(
        files_rack_app: true,
        wiki: true
      )

      # Override Bootstrap SASS variables
      self.bootstrap = OpenStruct.new(
        navbar_inverse_bg: '#53565a',
        navbar_inverse_link_color: '#fff',
        navbar_inverse_color: '$navbar-inverse-link-color',
        navbar_inverse_link_hover_color: 'darken($navbar-inverse-link-color, 20%)',
        navbar_inverse_brand_color: '$navbar-inverse-link-color',
        navbar_inverse_brand_hover_color: '$navbar-inverse-link-hover-color'
      )
      ENV.each {|k, v| /^BOOTSTRAP_(?<name>.+)$/ =~ k ? self.bootstrap[name.downcase] = v : nil}

      self.enable_log_formatter = ::Rails.env.production?
    end