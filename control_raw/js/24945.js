function (range, min, dataTypeName) {
      // 疑是 id 字段
      if (utils.isLikeId(dataTypeName)) {
        return utils.getId();
      }
      // 疑是 xxx time/date 字段, 返回当前时间之前一个月内的随机时间
      if (utils.isLikeTime(dataTypeName) || utils.isLikeDate(dataTypeName)) {
        return Date.now() - this._getNum(2592000);
      }
      // range 为 undefined 或者 null
      range = range == undefined ? 100000 : range;
      min = min == undefined ? 0 : min;
      return Math.floor(Math.random() * (range - min + 1) + min);
    }