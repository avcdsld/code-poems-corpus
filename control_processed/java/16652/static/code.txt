public static Checkpoint lastCheckpoint(File rootDir){
        List<Checkpoint> all = availableCheckpoints(rootDir);
        if(all.isEmpty()){
            return null;
        }
        return all.get(all.size()-1);
    }