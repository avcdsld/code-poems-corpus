def class_from_string(field)
      str = field.to_s.split('_').map(&:capitalize!).join
      str = 'Vulnerability' if str == 'Vulnerabilities'
      str.chop! if str.end_with?('s')
      Object.const_get('Nexpose').const_get(str)
    end