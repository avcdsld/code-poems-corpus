def full_regex_for_data(data, type, country_optional = true)
      regex = []
      regex << '0{2}?'
      regex << "(#{data[Core::INTERNATIONAL_PREFIX]})?"
      regex << "(#{data[Core::COUNTRY_CODE]})#{country_optional ? '?' : ''}"
      regex << "(#{data[Core::NATIONAL_PREFIX_FOR_PARSING] || data[Core::NATIONAL_PREFIX]})?"
      regex << "(#{type_regex(data[Core::TYPES][Core::GENERAL], type)})" if data[Core::TYPES]

      cr("^#{regex.join}$")
    end