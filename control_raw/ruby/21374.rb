def scrape()
      # Call prepare with the document, but before doing anything else.
      prepare document
      # Retrieve the document. This may raise HTTPError or HTMLParseError.
      case document
      when Array
        stack = @document.reverse # see below
      when HTML::Node
        # If a root element is specified, start selecting from there.
        # The stack is empty if we can't find any root element (makes
        # sense). However, the node we're going to process may be
        # a tag, or an HTML::Document.root which is the equivalent of
        # a document fragment.
        root_element = option(:root_element)
        root = root_element ? @document.find(:tag=>root_element) : @document
        stack = root ? (root.tag? ? [root] : root.children.reverse) : []
      else
        return
      end
      # @skip stores all the elements we want to skip (see #skip).
      # rules stores all the rules we want to process with this
      # scraper, based on the class definition.
      @skip = []
      @stop = false
      rules = self.class.rules.clone
      begin
        # Process the document one node at a time. We process elements
        # from the end of the stack, so each time we visit child elements,
        # we add them to the end of the stack in reverse order.
        while node = stack.pop
          break if @stop
          skip_this = false
          # Only match nodes that are elements, ignore text nodes.
          # Also ignore any element that's on the skip list, and if
          # found one, remove it from the list (since we never visit
          # the same element twice). But an element may be added twice
          # to the skip list.
          # Note: equal? is faster than == for nodes.
          next unless node.tag?
          @skip.delete_if { |s| skip_this = true if s.equal?(node) }
          next if skip_this

          # Run through all the rules until we process the element or
          # run out of rules. If skip_this=true then we processed the
          # element and we can break out of the loop. However, we might
          # process (and skip) descedants so also watch the skip list.
          rules.delete_if do |selector, extractor, rule_name, first_only|
            break if skip_this
            # The result of calling match (selected) is nil, element
            # or array of elements. We turn it into an array to
            # process one element at a time. We process all elements
            # that are not on the skip list (we haven't visited
            # them yet).
            if selected = selector.match(node, first_only)
              selected = [selected] unless selected.is_a?(Array)
              selected = [selected.first] if first_only
              selected.each do |element|
                # Do not process elements we already skipped
                # (see above). However, this time we may visit
                # an element twice, since selected elements may
                # be descendants of the current element on the
                # stack. In rare cases two elements on the stack
                # may pick the same descendants.
                next if @skip.find { |s| s.equal?(element) }
                # Call the extractor method with this element.
                # If it returns true, skip the element and if
                # the current element, don't process any more
                # rules. Again, pay attention to descendants.
                if extractor.bind(self).call(element)
                  @extracted = true
                end
                if @skip.delete(true)
                  if element.equal?(node)
                    skip_this = true
                  else
                    @skip << element
                  end
                end
              end
              first_only if !selected.empty?
            end
          end

          # If we did not skip the element, we're going to process its
          # children. Reverse order since we're popping from the stack.
          if !skip_this && children = node.children
            stack.concat children.reverse
          end
        end
      ensure
        @skip = nil
      end
      collect
      return result
    end