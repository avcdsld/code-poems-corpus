def file_name=(file_name)
      err = GPGME::gpgme_data_set_file_name(self, file_name)
      exc = GPGME::error_to_exception(err)
      raise exc if exc
      file_name
    end