function brushDataAdapter(dataLine) {
    return dataLine.dataByDate.map(function(d){
        d.value = d.topics.reduce(function(acc, topic) {
            return acc + topic.value;
        },0);

        return d;
    })
}