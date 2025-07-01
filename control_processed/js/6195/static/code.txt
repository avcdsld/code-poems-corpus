function filterAttributes(at) {
	return (
		!ignoredAttributes.includes(at.name) &&
		at.name.indexOf(':') === -1 &&
		(!at.value || at.value.length < MAXATTRIBUTELENGTH)
	);
}