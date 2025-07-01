public static String versionInfoString(Detail detail) {
        StringBuilder sb = new StringBuilder();
        for(VersionInfo grp : getVersionInfos()){
            sb.append(grp.getGroupId()).append(" : ").append(grp.getArtifactId()).append(" : ").append(grp.getBuildVersion());
            switch (detail){
                case FULL:
                case GAVC:
                    sb.append(" - ").append(grp.getCommitIdAbbrev());
                    if(detail != Detail.FULL) break;

                    sb.append("buildTime=").append(grp.getBuildTime()).append("branch=").append(grp.getBranch())
                            .append("commitMsg=").append(grp.getCommitMessageShort());
            }
            sb.append("\n");
        }
        return sb.toString();
    }