function move(delta) {
    const { state } = this;
    const { index, items, itemsPerSlide, autoplayInterval, slideWidth, gap, peek, config } = state;
    const nextIndex = getNextIndex(state, delta);
    let offsetOverride;

    config.preserveItems = true;
    this.isMoving = true;

    // When we are in autoplay mode we overshoot the desired index to land on a clone
    // of one of the ends. Then after the transition is over we update to the proper position.
    if (autoplayInterval) {
        if (delta === RIGHT && nextIndex < index) {
            // Transitions to one slide before the beginning.
            offsetOverride = -slideWidth - gap;

            // Move the items in the last slide to be before the first slide.
            for (let i = Math.ceil(itemsPerSlide + peek); i--;) {
                const item = items[items.length - i - 1];
                item.transform = `translateX(${(getMaxOffset(state) + slideWidth + gap) * -1}px)`;
            }
        } else if (delta === LEFT && nextIndex > index) {
            // Transitions one slide past the end.
            offsetOverride = getMaxOffset(state) + slideWidth + gap;

            // Moves the items in the first slide to be after the last slide.
            for (let i = Math.ceil(itemsPerSlide + peek); i--;) {
                const item = items[i];
                item.transform = `translateX(${(getMaxOffset(state) + slideWidth + gap)}px)`;
            }
        }

        config.offsetOverride = offsetOverride;
    }

    this.setState('index', nextIndex);
    this.once('carousel-update', () => {
        this.isMoving = false;

        if (offsetOverride !== undefined) {
            // If we are in autoplay mode and went outside of the normal offset
            // We make sure to restore all of the items that got moved around.
            items.forEach(item => { item.transform = undefined; });
        }
    });

    return nextIndex;
}