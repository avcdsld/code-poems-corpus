def save_to(saveToFile = nil)
			id = save()

			if id == nil || id == ""
				return false
			end			
			
			#Wait for it to be possibly ready
			sleep((@request.options().startDelay() / 1000) + 3)

			#Wait for it to be ready.
			while true do
				status = get_status(id)

				if !status.cached && !status.processing
					raise GrabzItException.new("The capture did not complete with the error: " + status.message, GrabzItException::RENDERING_ERROR)
					break
				elsif status.cached
					result = get_result(id)
					if !result
						raise GrabzItException.new("The capture could not be found on GrabzIt.", GrabzItException::RENDERING_MISSING_SCREENSHOT)
						break
					end
					
					if saveToFile == nil || saveToFile == ""
						return result
					end					

					screenshot = File.new(saveToFile, "wb")
					screenshot.write(result)
					screenshot.close

					break
				end

				sleep(3)
			end

			return true
		end