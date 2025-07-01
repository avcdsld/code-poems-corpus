public String getAuthorizationHeader(ProtectedResourceDetails details, OAuthConsumerToken accessToken, URL url, String httpMethod, Map<String, String> additionalParameters) {
    if (!details.isAcceptsAuthorizationHeader()) {
      return null;
    }
    else {
      Map<String, Set<CharSequence>> oauthParams = loadOAuthParameters(details, url, accessToken, httpMethod, additionalParameters);
      String realm = details.getAuthorizationHeaderRealm();

      StringBuilder builder = new StringBuilder("OAuth ");
      boolean writeComma = false;
      if (realm != null) { //realm is optional.
        builder.append("realm=\"").append(realm).append('"');
        writeComma = true;
      }

      for (Map.Entry<String, Set<CharSequence>> paramValuesEntry : oauthParams.entrySet()) {
        Set<CharSequence> paramValues = paramValuesEntry.getValue();
        CharSequence paramValue = findValidHeaderValue(paramValues);
        if (paramValue != null) {
          if (writeComma) {
            builder.append(", ");
          }

          builder.append(paramValuesEntry.getKey()).append("=\"").append(oauthEncode(paramValue.toString())).append('"');
          writeComma = true;
        }
      }

      return builder.toString();
    }
  }