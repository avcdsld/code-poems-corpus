def send(files)
      # Prepare the DICOM object(s):
      objects, success, message = load_files(files)
      if success
        # Open a DICOM link:
        establish_association
        if association_established?
          if request_approved?
            # Continue with our c-store operation, since our request was accepted.
            # Handle the transmission:
            perform_send(objects)
          end
        end
        # Close the DICOM link:
        establish_release
      else
        # Failed when loading the specified parameter as DICOM file(s). Will not transmit.
        logger.error(message)
      end
    end