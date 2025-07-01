function initTernServer(env, files) {
    ternOptions = {
        defs: env,
        async: true,
        getFile: getFile,
        plugins: {requirejs: {}, doc_comment: true, angular: true},
        ecmaVersion: 9
    };

    // If a server is already created just reset the analysis data before marking it for GC
    if (ternServer) {
        ternServer.reset();
        Infer.resetGuessing();
    }
        
    ternServer = new Tern.Server(ternOptions);

    files.forEach(function (file) {
        ternServer.addFile(file);
    });

}