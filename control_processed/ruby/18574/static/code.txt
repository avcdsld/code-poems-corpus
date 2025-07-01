def error_rendering(exception, symbol)
      Rails.logger.error exception

      @exception = exception
      @symbol = symbol
      @code = Rack::Utils::SYMBOL_TO_STATUS_CODE[symbol].to_i
      respond_with @exception, status: @code, template: ERROR_PATH, prefixes: _prefixes
    end