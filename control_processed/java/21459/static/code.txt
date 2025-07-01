public static Strictness determineStrictness(Stubbing stubbing, MockCreationSettings mockSettings, Strictness testLevelStrictness) {
        if (stubbing != null && stubbing.getStrictness() != null) {
            return stubbing.getStrictness();
        }

        if (mockSettings.isLenient()) {
            return Strictness.LENIENT;
        }

        return testLevelStrictness;
    }