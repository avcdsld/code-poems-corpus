@Restricted(NoExternalUse.class)
    public void setExecutable(Executable executable) {
        this.executable = executable;
        if (executable instanceof Run) {
            ((Run) executable).setQueueId(context.item.getId());
        }
    }