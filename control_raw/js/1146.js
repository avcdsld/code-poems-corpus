function transpileDerivedExchangeClass (contents) {

    let exchangeClassDeclarationMatches = contents.match (/^module\.exports\s*=\s*class\s+([\S]+)\s+extends\s+([\S]+)\s+{([\s\S]+?)^};*/m)

    // log.green (file, exchangeClassDeclarationMatches[3])

    let className = exchangeClassDeclarationMatches[1]
    let baseClass = exchangeClassDeclarationMatches[2]

    let methods = exchangeClassDeclarationMatches[3].trim ().split (/\n\s*\n/)

    let python2 = []
    let python3 = []
    let php = []

    let methodNames = []

    // run through all methods
    for (let i = 0; i < methods.length; i++) {
        // parse the method signature
        let part = methods[i].trim ()
        let lines = part.split ("\n")
        let signature = lines[0].trim ()
        let methodSignatureRegex = /(async |)([\S]+)\s\(([^)]*)\)\s*{/ // signature line
        let matches = methodSignatureRegex.exec (signature)

        if (!matches) {
            log.red (methods[i])
            log.yellow.bright ("\nMake sure your methods don't have empty lines!\n")
        }

        // async or not
        let keyword = matches[1]
        // try {
        //     keyword = matches[1]
        // } catch (e) {
        //     log.red (e)
        //     log.green (methods[i])
        //     log.yellow (exchangeClassDeclarationMatches[3].trim ().split (/\n\s*\n/))
        //     process.exit ()
        // }

        // method name
        let method = matches[2]

        methodNames.push (method)

        method = unCamelCase (method)

        // method arguments
        let args = matches[3].trim ()

        // extract argument names and local variables
        args = args.length ? args.split (',').map (x => x.trim ()) : []

        // get names of all method arguments for later substitutions
        let variables = args.map (arg => arg.split ('=').map (x => x.trim ()) [0])

        // add $ to each argument name in PHP method signature
        let phpArgs = args.join (', $').trim ().replace (/undefined/g, 'null').replace ('{}', 'array ()')
        phpArgs = phpArgs.length ? ('$' + phpArgs) : ''

        // remove excessive spacing from argument defaults in Python method signature
        let pythonArgs = args.map (x => x.replace (' = ', '='))
                                .join (', ')
                                .replace (/undefined/g, 'None')
                                .replace (/false/g, 'False')
                                .replace (/true/g, 'True')

        // method body without the signature (first line)
        // and without the closing bracket (last line)
        let js = lines.slice (1, -1).join ("\n")

        // transpile everything
        let { python3Body, python2Body, phpBody } = transpileJavaScriptToPythonAndPHP ({ js, className, variables, removeEmptyLines: true })

        // compile the final Python code for the method signature
        let pythonString = 'def ' + method + '(self' + (pythonArgs.length ? ', ' + pythonArgs : '') + '):'

        // compile signature + body for Python 2
        python2.push ('');
        python2.push ('    ' + pythonString);
        python2.push (python2Body);

        // compile signature + body for Python 3
        python3.push ('');
        python3.push ('    ' + keyword + pythonString);
        python3.push (python3Body);

        // compile signature + body for PHP
        php.push ('');
        php.push ('    public function ' + method + ' (' + phpArgs + ') {');
        php.push (phpBody);
        php.push ('    }')

    }

    return {

        // altogether in PHP, Python 2 and 3
        python2: createPythonClass (className, baseClass, python2, methodNames),
        python3: createPythonClass (className, baseClass, python3, methodNames, true),
        php:     createPHPClass    (className, baseClass, php,     methodNames),

        className,
        baseClass,
    }
}