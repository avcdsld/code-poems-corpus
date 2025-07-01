public double getMatchRatio(String strA, String strB) {
        if (strA == null && strB == null) {
            return MAX_RATIO;
            
        } else if (strA == null || strB == null) {
            return MIN_RATIO;
        }
        
        if (strA.isEmpty() && strB.isEmpty()) {
            return MAX_RATIO;
            
        } else if (strA.isEmpty() || strB.isEmpty()) {
            return MIN_RATIO;
        }
                
        //get the percentage match against the longer of the 2 strings
        return (double)getLCS(strA, strB).length() / Math.max(strA.length(), strB.length());
    }