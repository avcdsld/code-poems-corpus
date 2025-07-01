def bmap_btree_record_to_block_pointers(record, block_pointers_length)
      block_pointers = []
      # Fill in the missing blocks with 0-blocks
      block_pointers << 0 while (block_pointers_length + block_pointers.length) < record.start_offset
      1.upto(record.block_count) { |i| block_pointers << record.start_block + i - 1 }
      @block_offset += record.block_count
      block_pointers
    end