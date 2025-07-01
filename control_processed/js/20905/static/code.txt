function runDisambiguator(disambiguateRules, word){
		var result = undefined;
	
		for(var i in disambiguateRules){
	    	result = disambiguateRules[i](word);
	    	if(find(result)){
	    		break;
	    	}
	    }
	    
	    if(result==undefined){
	    	this.current_word = word;
	    	this.removal = undefined;
	    	return this;
	    }

	    return createResultObject(result, word, "DP");
	}