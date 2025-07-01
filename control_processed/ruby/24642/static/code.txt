def signature_hash(input_index: nil, output_script: nil, hash_type: BTC::SIGHASH_ALL, version: 0, amount: 0)

      raise ArgumentError, "Should specify input_index in Transaction#signature_hash." if !input_index
      raise ArgumentError, "Should specify output_script in Transaction#signature_hash." if !output_script
      raise ArgumentError, "Should specify hash_type in Transaction#signature_hash." if !hash_type

      # Create a temporary copy of the transaction to apply modifications to it.
      tx = self.dup

      # Note: BitcoinQT returns a 256-bit little-endian number 1 in such case,
      # but it does not matter because it would crash before that in CScriptCheck::operator()().
      # We normally won't enter this condition if script machine is instantiated
      # with transaction and input index, but it's better to check anyway.
      if (input_index >= tx.inputs.size)
        raise ArgumentError, "Input index is out of bounds for transaction: #{input_index} >= #{tx.inputs.size}"
      end

      # In case concatenating two scripts ends up with two codeseparators,
      # or an extra one at the end, this prevents all those possible incompatibilities.
      # Note: this normally never happens because there is no use for OP_CODESEPARATOR.
      # But we have to do that cleanup anyway to not break on rare transaction that use that for lulz.
      # Also: we modify the same subscript which is used several times for multisig check,
      # but that's what BitcoinQT does as well.
      output_script.delete_opcode(BTC::OP_CODESEPARATOR)

      # Blank out other inputs' signature scripts
      # and replace our input script with a subscript (which is typically a full
      # output script from the previous transaction).
      tx.inputs.each do |txin|
        txin.signature_script = BTC::Script.new
      end
      tx.inputs[input_index].signature_script = output_script

      # Blank out some of the outputs depending on BTCSignatureHashType
      # Default is SIGHASH_ALL - all inputs and outputs are signed.
      if (hash_type & BTC::SIGHASH_OUTPUT_MASK) == BTC::SIGHASH_NONE
        # Wildcard payee - we can pay anywhere.
        tx.remove_all_outputs

        # Blank out others' input sequence numbers to let others update transaction at will.
        tx.inputs.each_with_index do |txin, i|
          if i != input_index
            tx.inputs[i].sequence = 0
          end
        end

      # Single mode assumes we sign an output at the same index as an input.
      # Outputs before the one we need are blanked out. All outputs after are simply removed.
      elsif (hash_type & BTC::SIGHASH_OUTPUT_MASK) == BTC::SIGHASH_SINGLE
        # Only lock-in the txout payee at same index as txin.
        output_index = input_index;

        # If output_index is out of bounds, BitcoinQT is returning a 256-bit little-endian 0x01 instead of failing with error.
        # We should do the same to stay compatible.
        if output_index >= tx.outputs.size
          return "\x01" + "\x00"*31
        end

        # All outputs before the one we need are blanked out. All outputs after are simply removed.
        # This is equivalent to replacing outputs with (i-1) empty outputs and a i-th original one.
        my_output = tx.outputs[output_index]
        tx.remove_all_outputs
        (0...output_index).each do |i|
          tx.add_output(BTC::TransactionOutput.new)
        end
        tx.add_output(my_output)

        # Blank out others' input sequence numbers to let others update transaction at will.
        tx.inputs.each_with_index do |txin, i|
          if i != input_index
            txin.sequence = 0
          end
        end
      end # if hashtype is none or single

      # Blank out other inputs completely. This is not recommended for open transactions.
      if (hash_type & BTC::SIGHASH_ANYONECANPAY) != 0
        input = tx.inputs[input_index]
        tx.remove_all_inputs
        tx.add_input(input)
      end

      # Important: we have to hash transaction together with its hash type.
      # Hash type is appended as a little endian uint32 unlike 1-byte suffix of the signature.
      data = tx.data + BTC::WireFormat.encode_uint32le(hash_type)
      hash = BTC.hash256(data)
      # puts ""
      # puts "SIGHASH[#{self.transaction_id}, input #{input_index}, hashtype 0x#{hash_type.to_s(16)}]: hash = #{BTC.id_from_hash(hash)}; tx = " + tx.inspect
      # puts ""
      return hash
    end