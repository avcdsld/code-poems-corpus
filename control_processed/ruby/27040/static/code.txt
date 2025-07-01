def columns(table_name, name = nil)#:nodoc:
      result = show_fields_from(table_name, name)

      columns = []
      result.each do |field|
        klass = \
          if field[1] =~ GEOMETRY_REGEXP
            ActiveRecord::ConnectionAdapters::SpatialMysqlColumn
          else
            ActiveRecord::ConnectionAdapters::MysqlColumn
          end
        columns << klass.new(field[0], field[4], field[1], field[2] == "YES")
      end

      result.free
      columns
    end