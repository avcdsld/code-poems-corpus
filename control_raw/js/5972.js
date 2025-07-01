function promptUser() {

    return inquirer.prompt([
        {
            type: "list",
            name: "purpose",
            message: "How would you like to use ESLint?",
            default: "problems",
            choices: [
                { name: "To check syntax only", value: "syntax" },
                { name: "To check syntax and find problems", value: "problems" },
                { name: "To check syntax, find problems, and enforce code style", value: "style" }
            ]
        },
        {
            type: "list",
            name: "moduleType",
            message: "What type of modules does your project use?",
            default: "esm",
            choices: [
                { name: "JavaScript modules (import/export)", value: "esm" },
                { name: "CommonJS (require/exports)", value: "commonjs" },
                { name: "None of these", value: "none" }
            ]
        },
        {
            type: "list",
            name: "framework",
            message: "Which framework does your project use?",
            default: "react",
            choices: [
                { name: "React", value: "react" },
                { name: "Vue.js", value: "vue" },
                { name: "None of these", value: "none" }
            ]
        },
        {
            type: "checkbox",
            name: "env",
            message: "Where does your code run?",
            default: ["browser"],
            choices: [
                { name: "Browser", value: "browser" },
                { name: "Node", value: "node" }
            ]
        },
        {
            type: "list",
            name: "source",
            message: "How would you like to define a style for your project?",
            default: "guide",
            choices: [
                { name: "Use a popular style guide", value: "guide" },
                { name: "Answer questions about your style", value: "prompt" },
                { name: "Inspect your JavaScript file(s)", value: "auto" }
            ],
            when(answers) {
                return answers.purpose === "style";
            }
        },
        {
            type: "list",
            name: "styleguide",
            message: "Which style guide do you want to follow?",
            choices: [
                { name: "Airbnb (https://github.com/airbnb/javascript)", value: "airbnb" },
                { name: "Standard (https://github.com/standard/standard)", value: "standard" },
                { name: "Google (https://github.com/google/eslint-config-google)", value: "google" }
            ],
            when(answers) {
                answers.packageJsonExists = npmUtils.checkPackageJson();
                return answers.source === "guide" && answers.packageJsonExists;
            }
        },
        {
            type: "input",
            name: "patterns",
            message: "Which file(s), path(s), or glob(s) should be examined?",
            when(answers) {
                return (answers.source === "auto");
            },
            validate(input) {
                if (input.trim().length === 0 && input.trim() !== ",") {
                    return "You must tell us what code to examine. Try again.";
                }
                return true;
            }
        },
        {
            type: "list",
            name: "format",
            message: "What format do you want your config file to be in?",
            default: "JavaScript",
            choices: ["JavaScript", "YAML", "JSON"]
        },
        {
            type: "confirm",
            name: "installESLint",
            message(answers) {
                const verb = semver.ltr(answers.localESLintVersion, answers.requiredESLintVersionRange)
                    ? "upgrade"
                    : "downgrade";

                return `The style guide "${answers.styleguide}" requires eslint@${answers.requiredESLintVersionRange}. You are currently using eslint@${answers.localESLintVersion}.\n  Do you want to ${verb}?`;
            },
            default: true,
            when(answers) {
                return answers.source === "guide" && answers.packageJsonExists && hasESLintVersionConflict(answers);
            }
        }
    ]).then(earlyAnswers => {

        // early exit if no style guide is necessary
        if (earlyAnswers.purpose !== "style") {
            const config = processAnswers(earlyAnswers);
            const modules = getModulesList(config);

            return askInstallModules(modules, earlyAnswers.packageJsonExists)
                .then(() => writeFile(config, earlyAnswers.format));
        }

        // early exit if you are using a style guide
        if (earlyAnswers.source === "guide") {
            if (!earlyAnswers.packageJsonExists) {
                log.info("A package.json is necessary to install plugins such as style guides. Run `npm init` to create a package.json file and try again.");
                return void 0;
            }
            if (earlyAnswers.installESLint === false && !semver.satisfies(earlyAnswers.localESLintVersion, earlyAnswers.requiredESLintVersionRange)) {
                log.info(`Note: it might not work since ESLint's version is mismatched with the ${earlyAnswers.styleguide} config.`);
            }
            if (earlyAnswers.styleguide === "airbnb" && earlyAnswers.framework !== "react") {
                earlyAnswers.styleguide = "airbnb-base";
            }

            const config = ConfigOps.merge(processAnswers(earlyAnswers), getConfigForStyleGuide(earlyAnswers.styleguide));
            const modules = getModulesList(config);

            return askInstallModules(modules, earlyAnswers.packageJsonExists)
                .then(() => writeFile(config, earlyAnswers.format));

        }

        if (earlyAnswers.source === "auto") {
            const combinedAnswers = Object.assign({}, earlyAnswers);
            const config = processAnswers(combinedAnswers);
            const modules = getModulesList(config);

            return askInstallModules(modules).then(() => writeFile(config, earlyAnswers.format));
        }

        // continue with the style questions otherwise...
        return inquirer.prompt([
            {
                type: "list",
                name: "indent",
                message: "What style of indentation do you use?",
                default: "tab",
                choices: [{ name: "Tabs", value: "tab" }, { name: "Spaces", value: 4 }]
            },
            {
                type: "list",
                name: "quotes",
                message: "What quotes do you use for strings?",
                default: "double",
                choices: [{ name: "Double", value: "double" }, { name: "Single", value: "single" }]
            },
            {
                type: "list",
                name: "linebreak",
                message: "What line endings do you use?",
                default: "unix",
                choices: [{ name: "Unix", value: "unix" }, { name: "Windows", value: "windows" }]
            },
            {
                type: "confirm",
                name: "semi",
                message: "Do you require semicolons?",
                default: true
            },
            {
                type: "list",
                name: "format",
                message: "What format do you want your config file to be in?",
                default: "JavaScript",
                choices: ["JavaScript", "YAML", "JSON"]
            }
        ]).then(answers => {
            const totalAnswers = Object.assign({}, earlyAnswers, answers);

            const config = processAnswers(totalAnswers);
            const modules = getModulesList(config);

            return askInstallModules(modules).then(() => writeFile(config, answers.format));
        });
    });
}