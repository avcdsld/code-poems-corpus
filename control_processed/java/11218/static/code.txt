public static EnvVars getRemote(VirtualChannel channel) throws IOException, InterruptedException {
        if(channel==null)
            return new EnvVars("N/A","N/A");
        return channel.call(new GetEnvVars());
    }