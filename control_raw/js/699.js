function CommandMatcher(commandMatcherShorthand)
{
    /**
     * Ensure the shorthand notation used to initialize the CommandMatcher has
     * all required values.
     *
     * @param commandMatcherShorthand  an object containing information about
     *                                 the CommandMatcher
     */
    this.validate = function(commandMatcherShorthand) {
        var msg = "CommandMatcher validation error:\n"
            + print_r(commandMatcherShorthand);
        if (!commandMatcherShorthand.command) {
            throw new CommandMatcherException(msg + 'no command specified!');
        }
        if (!commandMatcherShorthand.target) {
            throw new CommandMatcherException(msg + 'no target specified!');
        }
        if (commandMatcherShorthand.minMatches &&
            commandMatcherShorthand.maxMatches &&
            commandMatcherShorthand.minMatches >
            commandMatcherShorthand.maxMatches) {
            throw new CommandMatcherException(msg + 'minMatches > maxMatches!');
        }
    };

    /**
     * Initialize this object.
     *
     * @param commandMatcherShorthand  an object containing information used to
     *                                 initialize the CommandMatcher
     */
    this.init = function(commandMatcherShorthand) {
        this.validate(commandMatcherShorthand);
        
        this.command = commandMatcherShorthand.command;
        this.target = commandMatcherShorthand.target;
        this.value = commandMatcherShorthand.value || null;
        this.minMatches = commandMatcherShorthand.minMatches || 1;
        this.maxMatches = commandMatcherShorthand.maxMatches || 1;
        this.updateArgs = commandMatcherShorthand.updateArgs ||
            function(command, args) { return args; };
    };
    
    /**
     * Determines whether a given command matches. Updates args by "reference"
     * and returns true if it does; return false otherwise.
     *
     * @param command  the command to attempt to match
     */
    this.isMatch = function(command) {
        var re = new RegExp('^' + this.command + '$');
        if (! re.test(command.command)) {
            return false;
        }
        re = new RegExp('^' + this.target + '$');
        if (! re.test(command.target)) {
            return false;
        }
        if (this.value != null) {
            re = new RegExp('^' + this.value + '$');
            if (! re.test(command.value)) {
                return false;
            }
        }
        
        // okay, the command matches
        return true;
    };
    
    // initialization
    this.init(commandMatcherShorthand);
}