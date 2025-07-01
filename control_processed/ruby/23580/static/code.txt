def save(options = {})
      _run_save_callbacks do 
        raise GitModel::NullId unless self.id

        if new_record?
          raise GitModel::RecordExists if self.class.exists?(self.id)
        else
          raise GitModel::RecordDoesntExist unless self.class.exists?(self.id)
        end

        GitModel.logger.debug "Saving #{self.class.name} with id: #{id}"

        dir = File.join(self.class.db_subdir, self.id)

        transaction = options.delete(:transaction) || GitModel::Transaction.new(options) 
        result = transaction.execute do |t|
          # Write the attributes to the attributes file
          t.index.add(File.join(dir, 'attributes.json'), Yajl::Encoder.encode(attributes, nil, :pretty => true))

          # Write the blob files
          blobs.each do |name, data|
            t.index.add(File.join(dir, name), data)
          end
        end

        if result
          @path = dir
          @branch = transaction.branch
          @new_record = false
        end

        result
      end
    end