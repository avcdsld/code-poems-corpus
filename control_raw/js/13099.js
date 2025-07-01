async function runAction(browser, page, options, actionString) {

	// Find the first action that matches the given action string
	const action = module.exports.actions.find(foundAction => {
		return foundAction.match.test(actionString);
	});

	// If no action can be found, error
	if (!action) {
		throw new Error(`Failed action: "${actionString}" cannot be resolved`);
	}

	// Run the action
	options.log.debug(`Running action: ${actionString}`);
	await action.run(browser, page, options, actionString.match(action.match));
	options.log.debug('  ✔︎ action complete');
}