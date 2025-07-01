public static ClassName get(TypeElement element) {
    checkNotNull(element, "element == null");
    String simpleName = element.getSimpleName().toString();

    return element.getEnclosingElement().accept(new SimpleElementVisitor8<ClassName, Void>() {
      @Override public ClassName visitPackage(PackageElement packageElement, Void p) {
        return new ClassName(packageElement.getQualifiedName().toString(), null, simpleName);
      }

      @Override public ClassName visitType(TypeElement enclosingClass, Void p) {
        return ClassName.get(enclosingClass).nestedClass(simpleName);
      }

      @Override public ClassName visitUnknown(Element unknown, Void p) {
        return get("", simpleName);
      }

      @Override public ClassName defaultAction(Element enclosingElement, Void p) {
        throw new IllegalArgumentException("Unexpected type nesting: " + element);
      }
    }, null);
  }