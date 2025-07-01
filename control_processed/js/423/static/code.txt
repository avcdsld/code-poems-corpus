function diffData(oldData, newData) {
    var diffResult = [];

    newData.diff(oldData)
        .add(function (idx) {
            diffResult.push({cmd: '+', idx: idx});
        })
        .update(function (newIdx, oldIdx) {
            diffResult.push({cmd: '=', idx: oldIdx, idx1: newIdx});
        })
        .remove(function (idx) {
            diffResult.push({cmd: '-', idx: idx});
        })
        .execute();

    return diffResult;
}