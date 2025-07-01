public static String getURLString(String relativeToBase){
        if(relativeToBase.startsWith("/")){
            relativeToBase = relativeToBase.substring(1);
        }
        return baseURL + relativeToBase;
    }