def with(selector)
            @selectors[selector] = Selector.new selector unless @selectors.has_key? selector
            yield @current_node if @selectors[selector].matches? @current_node, @filtered_nodes
        end