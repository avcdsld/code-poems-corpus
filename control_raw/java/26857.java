public String getTrendingQuery(String sprintStartDate,
                                   String sprintEndDate, String sprintDeltaDate, String queryName) {
        ST st = (new STGroupDir(featureSettings.getQueryFolder(), '$', '$')).getInstanceOf(queryName);
        st.add("sprintStartDate", sprintStartDate);
        st.add("sprintEndDate", sprintEndDate);
        st.add("sprintDeltaDate", sprintDeltaDate);

        return st.render();
    }