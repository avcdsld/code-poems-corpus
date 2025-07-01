def set_teams
    	@xml_doc.elements.each("game/team[@home_team='false']") do |element| 
    		@away_team = element.attributes["name"]
    	end
    	@xml_doc.elements.each("game/team[@home_team='true']") do |element| 
    		@home_team = element.attributes["name"]
    	end
    end