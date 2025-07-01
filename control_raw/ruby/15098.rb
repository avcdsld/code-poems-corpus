def header(certificate)
      x5t = thumbprint(certificate)
      logger.verbose("Creating self signed JWT header with thumbprint: #{x5t}.")
      { TYPE => TYPE_JWT,
        ALGORITHM => RS256,
        THUMBPRINT => x5t }
    end