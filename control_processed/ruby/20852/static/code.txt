def convert_warning_list(list)
      list.map do |list|
        case list
        when :all then Warning.all_warnings
        when :whitespace
          [ExtraBlankLinesWarning, ExtraWhitespaceWarning,
           OperatorSpacing, MisalignedUnindentationWarning]
          else list
        end
      end.flatten
    end