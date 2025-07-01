private AstParameter parseList() {
    eatChar('[');
    char nextChar = skipWS();
    AstParameter res = isQuote(nextChar)? parseStringList() : parseNumList();
    eatChar(']');
    return res;
  }