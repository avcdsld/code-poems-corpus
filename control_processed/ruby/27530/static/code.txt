def compare_versions(first, second)
      raise ArgumentError, "bad version format, version=#{first}" unless first =~ Orientdb4r::Client::SERVER_VERSION_PATTERN
      raise ArgumentError, "bad version format, version=#{second}" unless second =~ Orientdb4r::Client::SERVER_VERSION_PATTERN

      firstv = /^(?:(\d+)\.)?(?:(\d+)\.)?(\*|\d+)/.match(first)[0]
      secondv = /^(?:(\d+)\.)?(?:(\d+)\.)?(\*|\d+)/.match(second)[0]

      rslt = 0
      rslt = 1 if firstv > secondv
      rslt = -1 if firstv < secondv

      yield rslt if block_given?

      rslt
    end