public static void writeModel(@NonNull Model model, @NonNull OutputStream stream, boolean saveUpdater)
            throws IOException {
        writeModel(model,stream,saveUpdater,null);
    }