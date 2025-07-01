function setPageTarget(options) {
		var pageName;
		var serviceRegistry = options.serviceRegistry;
		if (options.target) { // we have metadata
			if (options.searchService) {
				options.searchService.setLocationByMetaData(options.target, {index: "last"});
			}
			pageName = options.name || options.target.Name;
			pageItem = options.target;
			generateRelatedLinks.call(this, serviceRegistry, options.target, exclusions, options.commandService, options.makeAlternate);
		} else {
			pageName = options.name;
			generateRelatedLinks.call(this, serviceRegistry, {NoTarget: ""}, exclusions, options.commandService, options.makeAlternate);
		}
		title = options.title;
		if (!title) {
			if (pageName) {
				title = i18nUtil.formatMessage(messages["PageTitleFormat"], pageName, options.task);
			} else {
				title = options.task;
			}
		}
		window.document.title = title;
		customGlobalCommands.afterSetPageTarget.apply(this, arguments);
	}