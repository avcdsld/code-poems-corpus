def compute_fee_for_transaction(tx, fee_rate)
      # Return mining fee if set manually
      return fee if fee
      # Compute fees for this tx by composing a tx with properly sized dummy signatures.
      simulated_tx = tx.dup
      simulated_tx.inputs.each do |txin|
        txout_script = txin.transaction_output.script
        txin.signature_script = txout_script.simulated_signature_script(strict: false) || txout_script
      end
      return simulated_tx.compute_fee(fee_rate: fee_rate)
    end