private static Locale determineUsersSystemLocale() {
        Locale userloc = null;
        final Locale systloc = Constant.getSystemsLocale();
        // first, try full match
        for (String ls : LocaleUtils.getAvailableLocales()) {
            String[] langArray = ls.split("_");
            if (langArray.length == 1) {
                if (systloc.getLanguage().equals(langArray[0])) {
                    userloc = systloc;
                    break;
                }
            }

            if (langArray.length == 2) {
                if (systloc.getLanguage().equals(langArray[0]) && systloc.getCountry().equals(langArray[1])) {
                    userloc = systloc;
                    break;
                }
            }

            if (langArray.length == 3) {
                if (systloc.getLanguage().equals(langArray[0]) && systloc.getCountry().equals(langArray[1])
                        && systloc.getVariant().equals(langArray[2])) {
                    userloc = systloc;
                    break;
                }
            }
        }

        if (userloc == null) {
            // second, try partial language match
            for (String ls : LocaleUtils.getAvailableLocales()) {
                String[] langArray = ls.split("_");
                if (systloc.getLanguage().equals(langArray[0])) {
                    userloc = createLocale(langArray);
                    break;
                }
            }
        }

        return userloc;
    }