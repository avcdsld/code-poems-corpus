def parse(tokens = ARGV)
            @show_usage = nil
            @show_help = nil
            @errors = []
            begin
                pos_vals, kw_vals, rest_vals = classify_tokens(tokens)
                args = process_args(pos_vals, kw_vals, rest_vals) unless @show_help
            rescue NoSuchArgumentError => ex
                self.errors << ex.message
                @show_usage = true
            end
            (@show_usage || @show_help) ? false : args
        end