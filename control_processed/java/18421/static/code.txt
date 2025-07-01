public static OpPredicate nameEquals(final String name){
        return new OpPredicate() {
            @Override
            public boolean matches(SameDiff sameDiff, DifferentialFunction function) {
                return function.getOwnName().equals(name);
            }
        };
    }