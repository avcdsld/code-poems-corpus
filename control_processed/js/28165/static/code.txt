function($super, key, value, properties) {
            var keysToIgnore = {
                'chart.nullValueMode': true
            };

            if(key in keysToIgnore) {
                return;
            }
            $super(key, value, properties);
        }