def timers_get
      hash = {}
      hash[:hello] = default_timers_hello
      hash[:mshello] = default_timers_hello_msec
      hash[:hold] = default_timers_hold
      hash[:mshold] = default_timers_hold_msec
      str = config_get('interface_hsrp_group', 'timers', @get_args)
      return hash if str.nil?
      regexp = Regexp.new('(?<msec1>msec)?'\
               ' *(?<he>\d+) *(?<msec2>msec)? *(?<ho>\d+)')
      params = regexp.match(str)
      hash[:mshello] = true if params[:msec1]
      hash[:mshold] = true if params[:msec2]
      hash[:hello] = params[:he].to_i
      hash[:hold] = params[:ho].to_i
      hash
    end