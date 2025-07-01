def pre_build
            if @page_offset_table.nil?
                raise InvalidHintStreamObjectError, "No page offset hint table"
            end

            if @shared_objects_table.nil?
                raise InvalidHintStreamObjectError, "No shared objects hint table"
            end

            @data = ""
            save_table(@page_offset_table)
            save_table(@shared_objects_table,         :S)
            save_table(@thumbnails_table,             :T)
            save_table(@outlines_table,               :O)
            save_table(@threads_table,                :A)
            save_table(@named_destinations_table,     :E)
            save_table(@interactive_forms_table,      :V)
            save_table(@information_dictionary_table, :I)
            save_table(@logical_structure_table,      :C)
            save_table(@page_labels_table,            :L)
            save_table(@renditions_table,             :R)
            save_table(@embedded_files_table,         :B)

            super
        end