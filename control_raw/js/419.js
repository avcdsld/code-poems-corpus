function setDefault(levels, ecModel) {
    var globalColorList = ecModel.get('color');

    if (!globalColorList) {
        return;
    }

    levels = levels || [];
    var hasColorDefine;
    zrUtil.each(levels, function (levelDefine) {
        var model = new Model(levelDefine);
        var modelColor = model.get('color');

        if (model.get('itemStyle.color')
            || (modelColor && modelColor !== 'none')
        ) {
            hasColorDefine = true;
        }
    });

    if (!hasColorDefine) {
        var level0 = levels[0] || (levels[0] = {});
        level0.color = globalColorList.slice();
    }

    return levels;
}