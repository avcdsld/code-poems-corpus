function getVerbHelp(verb, output) {
    let targets = [];
    let options = {
        head: `Available resources for ${chalk.bold(verb)}:`,
        table: []
    };

    // special verbs

    let sections = [];

    switch (verb) {
    case "query":
        output.write(chalk.cyan.bold("luis query --query <querytext> [--appId | --endpoint | --nologging | --region | --spellCheck | --staging | --subscriptionKey | --timezoneOffset | --timing |  --verbose]\n\n"))
        options.table.push([chalk.cyan.bold("--query <query>"), "Query to analyze with LUIS prediction."]);
        options.table.push([chalk.cyan.bold("--endpoint <endpointUrl>"), "Endpoint to use for query like https://westus.api.cognitive.microsoft.com/luis/v2.0/apps, overrides region."]);
        options.table.push([chalk.cyan.bold("--nologging"), "Turn off query logging in LUIS."]);
        options.table.push([chalk.cyan.bold("--spellCheck <key>"), "Check spelling using your Bing spelling key."]);
        options.table.push([chalk.cyan.bold("--staging"), "Use the staging environtment rather than production."]);
        options.table.push([chalk.cyan.bold("--timezoneOffset <minutes>"), "Specify the timezone offset in minutes used for resolving data time."]);
        options.table.push([chalk.cyan.bold("--timing [iterations]"), "Perform timings on query, default is 5 iterations."]);
        options.table.push([chalk.cyan.bold("--verbose"), "Include scores for all intents."]);
        sections.push(options);
        sections.push(configSection);
        sections.push(globalArgs);
        return sections;

    case "set":
        output.write(chalk.cyan.bold("luis set <appIdOrName> [--appId|--versionId|--authoringKey|--endpoint] <value>\n\n"))
        options.table.push([chalk.cyan.bold("<appIdOrName>"), "change the active application by looking it up by name or id"]);
        options.table.push([chalk.cyan.bold("--appId <appId>"), "change the active application id "]);
        options.table.push([chalk.cyan.bold("--versionId <version>"), "change the active version id "]);
        options.table.push([chalk.cyan.bold("--authoringKey <authoringKey>"), "change the active authoringKey◘"]);
        options.table.push([chalk.cyan.bold("--endpoint <endpointUrl>"), "change the active endpointBasePath url"]);
        sections.push(options);
        sections.push(configSection);
        sections.push(globalArgs);
        return sections;
    }

    for (let iOperation in operations) {
        let operation = operations[iOperation];
        if (operation.methodAlias == verb) {
            let target = operation.target[0];
            if (targets.indexOf(target) < 0) {
                targets.push(target);
            }
        }
    }


    if (targets.length == 0)
        return getGeneralHelpContents(output);

    targets.sort();
    for (let target of targets) {
        options.table.push([chalk.cyan.bold(target), '']);
    }
    sections.push(options);
    sections.push(configSection);
    sections.push(globalArgs);
    return sections;
}