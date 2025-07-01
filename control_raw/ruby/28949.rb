def fetch_script_config
      sconf = fetch_machine_param :config
      sconf ||= {}
      extras = {
        :region => @@global.region,
        :zone => @@global.zone,
        :environment => @@global.environment,
        :role => @@global.role,
        :position => @@global.position
      }
      sconf.merge! extras
      sconf
    end