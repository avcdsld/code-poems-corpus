def remove_revision(index)
            if index < 0 or index > @revisions.size
                raise IndexError, "Not a valid revision index"
            end

            if @revisions.size == 1
                raise InvalidPDFError, "Cannot remove last revision"
            end

            @revisions.delete_at(index)
            self
        end