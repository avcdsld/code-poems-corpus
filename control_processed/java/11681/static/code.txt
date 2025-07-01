public String substitute(AbstractBuild<?,?> build, String text) {
        return Util.replaceMacro(text,createVariableResolver(build));
    }