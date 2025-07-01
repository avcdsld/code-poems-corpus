def append_presentation_contexts(presentation_contexts, item_type, request=false)
      # Iterate the abstract syntaxes:
      presentation_contexts.each_pair do |abstract_syntax, context_ids|
        # Iterate the context ids:
        context_ids.each_pair do |context_id, syntax|
          # PRESENTATION CONTEXT:
          # Presentation context item type (1 byte)
          @outgoing.encode_last(item_type, "HEX")
          # Reserved (1 byte)
          @outgoing.encode_last("00", "HEX")
          # Presentation context item length (2 bytes)
          ts_length = 4*syntax[:transfer_syntaxes].length + syntax[:transfer_syntaxes].join.length
          # Abstract syntax item only included in requests, not accepts:
          items_length = 4 + ts_length
          items_length += 4 + abstract_syntax.length if request
          @outgoing.encode_last(items_length, "US")
          # Presentation context ID (1 byte)
          @outgoing.encode_last(context_id, "BY")
          # Reserved (1 byte)
          @outgoing.encode_last("00", "HEX")
          # (1 byte) Reserved (for association request) & Result/reason (for association accept response)
          result = (syntax[:result] ? syntax[:result] : 0)
          @outgoing.encode_last(result, "BY")
          # Reserved (1 byte)
          @outgoing.encode_last("00", "HEX")
          ## ABSTRACT SYNTAX SUB-ITEM: (only for request, not response)
          if request
            # Abstract syntax item type (1 byte)
            @outgoing.encode_last(ITEM_ABSTRACT_SYNTAX, "HEX")
            # Reserved (1 byte)
            @outgoing.encode_last("00", "HEX")
            # Abstract syntax item length (2 bytes)
            @outgoing.encode_last(abstract_syntax.length, "US")
            # Abstract syntax (variable length)
            @outgoing.encode_last(abstract_syntax, "STR")
          end
          ## TRANSFER SYNTAX SUB-ITEM (not included if result indicates error):
          if result == ACCEPTANCE
            syntax[:transfer_syntaxes].each do |t|
              # Transfer syntax item type (1 byte)
              @outgoing.encode_last(ITEM_TRANSFER_SYNTAX, "HEX")
              # Reserved (1 byte)
              @outgoing.encode_last("00", "HEX")
              # Transfer syntax item length (2 bytes)
              @outgoing.encode_last(t.length, "US")
              # Transfer syntax (variable length)
              @outgoing.encode_last(t, "STR")
            end
          end
        end
      end
    end