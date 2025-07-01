public static SVGGlyph getIcoMoonGlyph(String glyphName) throws Exception{
        SVGGlyphBuilder builder = glyphsMap.get(glyphName);
        if(builder == null) throw new Exception("Glyph '" + glyphName + "' not found!");
        SVGGlyph glyph = builder.build();
        // we need to apply transformation to correct the icon since
        // its being inverted after importing from icomoon
        glyph.getTransforms().add(new Scale(1, -1));
        Translate height = new Translate();
        height.yProperty().bind(Bindings.createDoubleBinding(() -> -glyph.getHeight(), glyph.heightProperty()));
        glyph.getTransforms().add(height);
        return glyph;
    }