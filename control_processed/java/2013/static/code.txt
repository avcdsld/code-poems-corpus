public void addBodyFileUpload(String name, File file, String contentType, boolean isText)
            throws ErrorDataEncoderException {
        addBodyFileUpload(name, file.getName(), file, contentType, isText);
    }