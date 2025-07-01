def versions
      @versions ||=
        repo
        .tags
        .map(&:name)
        .select { |tag| tag =~ /(.*\..*\..*)/ }
        .map { |tag| Semverse::Version.try_new tag }
        .compact
    end