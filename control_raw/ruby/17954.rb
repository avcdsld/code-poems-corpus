def controller_dirs
			parts = @controller.class.underscore.split('/').map do |part|
				%w[_controller _ctrl]
					.find { |suffix| part.chomp! suffix }
				part
				## Alternative, but slower by ~50%:
				# part.sub(/_(controller|ctrl)$/, '')
			end
			combine_parts(parts).map! { |path| path.join('/') }
		end