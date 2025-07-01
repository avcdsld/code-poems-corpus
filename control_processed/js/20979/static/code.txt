function serializeTopics(topics) {
    return topics.map(function (topic) {
        if (typeof (topic) === 'string') {
            return topic;
        }
        else if (Array.isArray(topic)) {
            topic.forEach(function (topic) {
                if (topic !== null && bytes_1.hexDataLength(topic) !== 32) {
                    errors.throwError('invalid topic', errors.INVALID_ARGUMENT, { argument: 'topic', value: topic });
                }
            });
            return topic.join(',');
        }
        else if (topic === null) {
            return '';
        }
        return errors.throwError('invalid topic value', errors.INVALID_ARGUMENT, { argument: 'topic', value: topic });
    }).join('&');
}