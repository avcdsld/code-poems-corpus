def decrypt(passwd = "")
            raise EncryptionError, "PDF is not encrypted" unless self.encrypted?

            # Turn the encryption dictionary into a standard encryption dictionary.
            handler = trailer_key(:Encrypt)
            handler = self.cast_object(handler.reference, Encryption::Standard::Dictionary)

            unless handler.Filter == :Standard
                raise EncryptionNotSupportedError, "Unknown security handler : '#{handler.Filter}'"
            end

            doc_id = trailer_key(:ID)
            unless doc_id.is_a?(Array)
                raise EncryptionError, "Document ID was not found or is invalid" unless handler.V.to_i == 5
            else
                doc_id = doc_id.first
            end

            encryption_key = handler.derive_encryption_key(passwd, doc_id)

            self.extend(Encryption::EncryptedDocument)
            self.encryption_handler = handler
            self.encryption_key = encryption_key

            decrypt_objects

            self
        end