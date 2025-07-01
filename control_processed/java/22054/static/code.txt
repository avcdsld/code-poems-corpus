public static Optional<ElementKind> resolveKind(Element element) {
        if (element != null) {

            try {
                final ElementKind kind = element.getKind();
                return Optional.of(kind);
            } catch (Exception e) {
                // ignore and fall through to empty
            }
        }
        return Optional.empty();
    }