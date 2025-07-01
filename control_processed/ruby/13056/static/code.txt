def inline_gpg_to_chunks body, encoding_to, encoding_from
    lines = body.split("\n")

    # First case: Message is enclosed between
    #
    # -----BEGIN PGP SIGNED MESSAGE-----
    # and
    # -----END PGP SIGNED MESSAGE-----
    #
    # In some cases, END PGP SIGNED MESSAGE doesn't appear
    # (and may leave strange -----BEGIN PGP SIGNATURE----- ?)
    gpg = lines.between(GPG_SIGNED_START, GPG_SIGNED_END)
    # between does not check if GPG_END actually exists
    # Reference: http://permalink.gmane.org/gmane.mail.sup.devel/641
    if !gpg.empty?
      msg = RMail::Message.new
      msg.body = gpg.join("\n")

      body = body.transcode(encoding_to, encoding_from)
      lines = body.split("\n")
      sig = lines.between(GPG_SIGNED_START, GPG_SIG_START)
      startidx = lines.index(GPG_SIGNED_START)
      endidx = lines.index(GPG_SIG_END)
      before = startidx != 0 ? lines[0 .. startidx-1] : []
      after = endidx ? lines[endidx+1 .. lines.size] : []

      # sig contains BEGIN PGP SIGNED MESSAGE and END PGP SIGNATURE, so
      # we ditch them. sig may also contain the hash used by PGP (with a
      # newline), so we also skip them
      sig_start = sig[1].match(/^Hash:/) ? 3 : 1
      sig_end = sig.size-2
      payload = RMail::Message.new
      payload.body = sig[sig_start, sig_end].join("\n")
      return [text_to_chunks(before, false),
              CryptoManager.verify(nil, msg, false),
              message_to_chunks(payload),
              text_to_chunks(after, false)].flatten.compact
    end

    # Second case: Message is encrypted

    gpg = lines.between(GPG_START, GPG_END)
    # between does not check if GPG_END actually exists
    if !gpg.empty? && !lines.index(GPG_END).nil?
      msg = RMail::Message.new
      msg.body = gpg.join("\n")

      startidx = lines.index(GPG_START)
      before = startidx != 0 ? lines[0 .. startidx-1] : []
      after = lines[lines.index(GPG_END)+1 .. lines.size]

      notice, sig, decryptedm = CryptoManager.decrypt msg, true
      chunks = if decryptedm # managed to decrypt
        children = message_to_chunks(decryptedm, true)
        [notice, sig].compact + children
      else
        [notice]
      end
      return [text_to_chunks(before, false),
              chunks,
              text_to_chunks(after, false)].flatten.compact
    end
  end