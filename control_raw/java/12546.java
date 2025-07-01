public void beginType(String type, String kind, int modifiers,
      String extendsType, String... implementsTypes) throws IOException {
    indent();
    modifiers(modifiers);
    out.write(kind);
    out.write(" ");
    type(type);
    if (extendsType != null) {
      out.write("\n");
      indent();
      out.write("    extends ");
      type(extendsType);
    }
    if (implementsTypes.length > 0) {
      out.write("\n");
      indent();
      out.write("    implements ");
      for (int i = 0; i < implementsTypes.length; i++) {
        if (i != 0) {
          out.write(", ");
        }
        type(implementsTypes[i]);
      }
    }
    out.write(" {\n");
    pushScope(Scope.TYPE_DECLARATION);
  }