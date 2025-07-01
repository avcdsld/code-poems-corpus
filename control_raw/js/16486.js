function _mapDataLinkToD3Link(link, index, d3Links = [], config, state = {}) {
    // find the matching link if it exists
    const d3Link = d3Links.find(l => l.source.id === link.source && l.target.id === link.target);
    const customProps = utils.pick(link, LINK_CUSTOM_PROPS_WHITELIST);

    if (d3Link) {
        const toggledDirected = state.config && state.config.directed && config.directed !== state.config.directed;
        const refinedD3Link = {
            index,
            ...d3Link,
            ...customProps,
        };

        // every time we toggle directed config all links should be visible again
        if (toggledDirected) {
            return { ...refinedD3Link, isHidden: false };
        }

        // every time we disable collapsible (collapsible is false) all links should be visible again
        return config.collapsible ? refinedD3Link : { ...refinedD3Link, isHidden: false };
    }

    const highlighted = false;
    const source = {
        id: link.source,
        highlighted,
    };
    const target = {
        id: link.target,
        highlighted,
    };

    return {
        index,
        source,
        target,
        ...customProps,
    };
}