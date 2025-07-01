public static OpPredicate opNameMatches(final String regex){
        return new OpPredicate() {
            @Override
            public boolean matches(SameDiff sameDiff, DifferentialFunction function) {
                return function.getOwnName().matches(regex);
            }
        };
    }