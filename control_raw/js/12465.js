function (item, raw, content) {
            var self = this;
            var base = '../',
                baseItem,
                newWin = false,
                className = 'crosslink';

            item = fixType(item);

            item = baseItem = Y.Lang.trim(item.replace('{', '').replace('}', ''));
            //Remove Cruft
            item = item.replace('*', '').replace('[', '').replace(']', '');
            var link = false,
                href;

            if (self.data.classes[item]) {
                link = true;
            } else {
                if (self.data.classes[item.replace('.', '')]) {
                    link = true;
                    item = item.replace('.', '');
                }
            }
            if (self.options.externalData) {
                if (self.data.classes[item]) {
                    if (self.data.classes[item].external) {
                        href = self.data.classes[item].path;
                        base = self.options.externalData.base;
                        className += ' external';
                        newWin = true;
                        link = true;
                    }
                }
            }

            if (item.indexOf('/') > -1) {
                //We have a class + method to parse
                var parts = item.split('/'),
                    cls = parts[0],
                    method = parts[1],
                    type = 'method';

                if (method.indexOf(':') > -1) {
                    parts = method.split(':');
                    method = parts[0];
                    type = parts[1];
                    if (type.indexOf('attr') === 0) {
                        type = 'attribute';
                    }
                }

                if (cls && method) {
                    if (self.data.classes[cls]) {
                        self.data.classitems.forEach(function (i) {
                            if (i.itemtype === type && i.name === method && i.class === cls) {
                                link = true;
                                baseItem = method;
                                var t = type;
                                if (t === 'attribute') {
                                    t = 'attr';
                                }
                                href = Y.webpath(base, 'classes', cls + '.html#' + t + '_' + method);
                            }
                        });
                    }
                }

            }

            if (item === 'Object' || item === 'Array') {
                link = false;
            }
            if (!href) {
                href = Y.webpath(base, 'classes', item + '.html');
                if (base.match(/^https?:\/\//)) {
                    href = base + Y.webpath('classes', item + '.html');
                }
            }
            if (!link && self.options.linkNatives) {
                if (self.NATIVES && self.NATIVES[item]) {
                    href = self.NATIVES_LINKER(item);
                    if (href) {
                        className += ' external';
                        newWin = true;
                        link = true;
                    }
                }
            }
            if (link) {
                if (content !== undefined) {
                    content = content.trim();
                }
                if (!content) {
                    content = baseItem;
                }
                item = '<a href="' + href + '" class="' + className + '"' + ((newWin) ? ' target="_blank"' : '') + '>' + content + '</a>';
            }
            return (raw) ? href : item;
        }