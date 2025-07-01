function getCssomForAllRootNodes(rootNodes, convertDataToStylesheet, timeout) {
	const q = axe.utils.queue();

	rootNodes.forEach(({ rootNode, shadowId }, index) =>
		q.defer((resolve, reject) =>
			loadCssom({
				rootNode,
				shadowId,
				timeout,
				convertDataToStylesheet,
				rootIndex: index + 1
			})
				.then(resolve)
				.catch(reject)
		)
	);

	return q;
}