public static List<Variable> getRunTimeVariables(
      final Collection<Variable> variables) {
    final List<Variable> runtimeVariables =
        ReportalUtil.getVariablesByRegex(variables,
            Reportal.REPORTAL_CONFIG_PREFIX_NEGATION_REGEX);

    return runtimeVariables;
  }