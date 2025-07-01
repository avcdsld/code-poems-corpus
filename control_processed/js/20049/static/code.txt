function getNeighboringChart(chartItem, neighboringWeek) {
	if (neighboringWeek == NeighboringWeek.Previous) {
		if (chartItem[0].attribs.class.indexOf('dropdown__date-selector-option--disabled') == -1) {
			return {
				url: BILLBOARD_BASE_URL + chartItem[0].children[1].attribs.href,
				date: chartItem[0].children[1].attribs.href.split('/')[3]
			};
		}
	} else {
		if (chartItem[1].attribs.class.indexOf('dropdown__date-selector-option--disabled') == -1) {
			return {
				url: BILLBOARD_BASE_URL + chartItem[1].children[1].attribs.href,
				date: chartItem[1].children[1].attribs.href.split('/')[3]
			};
		}
	}
	return {
		url: '',
		date: ''
	}
}