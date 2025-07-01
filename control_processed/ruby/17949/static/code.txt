def path_of(route_or_controller, action = nil)
			if route_or_controller.is_a?(Flame::Router::Route)
				route = route_or_controller
				controller = route.controller
				action = route.action
			else
				controller = route_or_controller
			end
			reverse_routes.dig(controller.to_s, action)
		end