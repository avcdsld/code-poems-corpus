def embedded_targets_in_native_target(native_target)
      native_targets.select do |target|
        host_targets_for_embedded_target(target).map(&:uuid).include? native_target.uuid
      end
    end