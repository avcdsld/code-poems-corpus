function replacePlaceholders(src, options) {
	return Object.keys(placeholders).reduce((out, placeholder) => {
		return out.replace(new RegExp(`${placeholder}`, 'g'), placeholders[placeholder]);
	}, src);
}