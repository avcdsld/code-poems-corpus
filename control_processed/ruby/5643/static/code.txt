def present?
      displayed = display_check
      if displayed.nil? && display_check
        Watir.logger.deprecate 'Checking `#present? == false` to determine a stale element',
                               '`#stale? == true`',
                               reference: 'http://watir.com/staleness-changes',
                               ids: [:stale_present]
      end
      displayed
    rescue UnknownObjectException, UnknownFrameException
      false
    end