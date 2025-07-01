public static AbstractServerPredicate ofServerPredicate(final Predicate<Server> p) {
        return new AbstractServerPredicate() {
            @Override
            @edu.umd.cs.findbugs.annotations.SuppressWarnings(value = "NP")
            public boolean apply(PredicateKey input) {
                return p.apply(input.getServer());
            }            
        };        
    }