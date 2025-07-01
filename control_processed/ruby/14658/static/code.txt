def parse_options(args) # :nodoc:
      option_parser_class = self.class.const_get("#{options[:subcommand_option_handling_strategy].to_s.capitalize}CommandOptionParser")
      OptionParsingResult.new.tap { |parsing_result|
        parsing_result.arguments = args
        parsing_result = @global_option_parser.parse!(parsing_result)
        option_parser_class.new(@accepts).parse!(parsing_result, options[:argument_handling_strategy])
      }
    end