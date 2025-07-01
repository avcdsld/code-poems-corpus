def export
            exported_obj = self.logicalize
            exported_obj.no = exported_obj.generation = 0
            exported_obj.set_document(nil) if exported_obj.indirect?
            exported_obj.parent = nil
            exported_obj.xref_cache.clear

            exported_obj
        end