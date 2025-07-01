public final String getBuildNowText() {
        return isParameterized() ? AlternativeUiTextProvider.get(BUILD_NOW_TEXT, asJob(), Messages.ParameterizedJobMixIn_build_with_parameters())
                : AlternativeUiTextProvider.get(BUILD_NOW_TEXT, asJob(), Messages.ParameterizedJobMixIn_build_now());
    }