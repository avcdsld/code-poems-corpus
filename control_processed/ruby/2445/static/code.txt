def compiler_swift_version(user_version)
      return LATEST_SWIFT_VERSION unless user_version

      LONG_SWIFT_VERSIONS.select do |version|
        user_version.start_with?(version)
      end.last || "#{user_version[0]}.0"
    end