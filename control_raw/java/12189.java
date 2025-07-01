public void parse(InputStream script, Binding binding) {
        if (script==null)
            throw new IllegalArgumentException("No script is provided");
        setBinding(binding);
        CompilerConfiguration cc = new CompilerConfiguration();
        cc.setScriptBaseClass(ClosureScript.class.getName());
        GroovyShell shell = new GroovyShell(classLoader,binding,cc);

        ClosureScript s = (ClosureScript)shell.parse(new InputStreamReader(script));
        s.setDelegate(this);
        s.run();
    }