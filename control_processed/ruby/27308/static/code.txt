def rest_arg(key, desc, opts = {}, &block)
            self << ArgParser::RestArgument.new(key, desc, opts, &block)
        end