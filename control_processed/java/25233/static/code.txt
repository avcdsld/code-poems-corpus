private String[] getEncodingMapKeys(Env env, Env.StackHelp stk, AstRoot asts[]) {
    return getArgAsStrings(env, stk, asts[1]);
  }