def load_all_objects
            return if loaded? or @parser.nil?

            @revisions.each do |revision|
                if revision.xreftable?
                    xrefs = revision.xreftable
                elsif revision.xrefstm?
                    xrefs = revision.xrefstm
                else
                    next
                end

                xrefs.each_with_number do |xref, no|
                    self.get_object(no) unless xref.free?
                end
            end

            loaded!
        end