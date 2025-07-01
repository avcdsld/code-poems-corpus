def export_grid_if_requested(opts = {})
      grid = self.wice_grid_instances.detect(&:output_csv?)

      if grid
        template_name = opts[grid.name] || opts[grid.name.intern]
        template_name ||= grid.name + '_grid'
        temp_filename = render_to_string(partial: template_name)
        temp_filename = temp_filename.strip
        filename = (grid.csv_file_name || grid.name) + '.csv'
        grid.csv_tempfile.close
        send_file_rails2 temp_filename, filename: filename, type: "text/csv; charset=#{get_output_encoding grid.csv_encoding}"
        grid.csv_tempfile = nil
        true
      else
        yield if block_given?
        false
      end
    end