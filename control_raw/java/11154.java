public AbstractProject<?,?> getRootProject() {
        if (this instanceof TopLevelItem) {
            return this;
        } else {
            ItemGroup p = this.getParent();
            if (p instanceof AbstractProject)
                return ((AbstractProject) p).getRootProject();
            return this;
        }
    }