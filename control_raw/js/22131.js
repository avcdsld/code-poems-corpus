function() {
                // 获取现有颜色映射
                //     resource => color_index
                var colorMapping = this._getResourceColorIndexMapping();

                var resource, used, i;

                used = [];

                // 抽取已经使用的值到 used 数组
                for (resource in colorMapping) {
                    if (Object.prototype.hasOwnProperty.call(colorMapping, resource)) {
                        used.push(colorMapping[resource]);
                    }
                }

                // 枚举所有的可用值，如果还没被使用，返回
                for (i = 0; i < RESOURCE_COLOR_SERIES.length; i++) {
                    if (!~used.indexOf(i)) return i;
                }

                // 没有可用的颜色了
                return -1;
            }