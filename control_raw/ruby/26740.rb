def fetch(atom_names, start=false)
      atoms = ActiveSupport::OrderedHash.new

      atom_names.uniq.collect{|a| encoded_prefix(a) }.uniq.each do |prefix|
        pattern = @path.join(prefix.to_s).to_s
        pattern += '*' if start
        pattern += INDEX_FILE_EXTENSION

        Pathname.glob(pattern).each do |atom_file|
          atom_file.open do |f|
            atoms.merge!(Marshal.load(f))
          end
        end # Pathname.glob

      end # atom_names.uniq
      atoms
    end