public static FormValidation error(String message) {
        return errorWithMarkup(message==null?null: Util.escape(message));
    }