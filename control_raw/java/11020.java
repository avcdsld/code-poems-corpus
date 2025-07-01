public static @Nonnull String getValue(@Nonnull String xpath, @Nonnull File file, @Nonnull String fileDataEncoding) throws IOException, SAXException, XPathExpressionException {
        Document document = parse(file, fileDataEncoding);
        return getValue(xpath, document);
    }