def load_object_at_offset(revision, offset)
            return nil if loaded? or @parser.nil?
            pos = @parser.pos

            begin
                object = @parser.parse_object(offset)
                return nil if object.nil?

                if self.is_a?(Encryption::EncryptedDocument)
                    make_encrypted_object(object)
                end

                add_to_revision(object, revision)
            ensure
                @parser.pos = pos
            end

            object
        end