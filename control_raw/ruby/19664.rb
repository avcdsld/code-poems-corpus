def retrogress_bbtree
      if @tags_list[-1].definition[:self_closable]
        # It is possible that the next (self_closable) tag is on the next line
        # Remove newline of current tag and parent tag as they are (probably) not intented as an actual newline here but as tag separator
        @tags_list[-1][:nodes][0][:text].chomp! unless @tags_list[-1][:nodes][0][:text].nil?
        @tags_list[-2][:nodes][0][:text].chomp! unless @tags_list.length < 2 or @tags_list[-2][:nodes][0][:text].nil?
      end

      @tags_list.pop     # remove latest tag in tags_list since it's closed now...
      # The parsed data manifests in @bbtree.current_node.children << TagNode.new(element) which I think is more confusing than needed

      if within_open_tag?
        @current_node = @tags_list[-1]
      else # If we're still at the root of the BBTree or have returned back to the root via encountring closing tags...
        @current_node = TagNode.new({:nodes => self.nodes})  # Note:  just passing in self works too...
      end
    end