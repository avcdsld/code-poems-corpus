protected static String getStartingMessage() {
        DateFormat dateFormat = SimpleDateFormat.getDateTimeInstance(DateFormat.SHORT, DateFormat.MEDIUM);
        StringBuilder strBuilder = new StringBuilder(200);
        strBuilder.append(Constant.PROGRAM_NAME).append(' ').append(Constant.PROGRAM_VERSION);
        strBuilder.append(" started ");
        strBuilder.append(dateFormat.format(new Date()));
        strBuilder.append(" with home ").append(Constant.getZapHome());
        return strBuilder.toString();
    }