function configureWrapper(name){
                        var _ = nvd3Utils.deepExtend(defaultWrapper(name), scope.options[name] || {});

                        if (scope._config.extended) scope.options[name] = _;

                        var wrapElement = angular.element('<div></div>').html(_['html'] || '')
                            .addClass(name).addClass(_.className)
                            .removeAttr('style')
                            .css(_.css);

                        if (!_['html']) wrapElement.text(_.text);

                        if (_.enable) {
                            if (name === 'title') element.prepend(wrapElement);
                            else if (name === 'subtitle') angular.element(element[0].querySelector('.title')).after(wrapElement);
                            else if (name === 'caption') element.append(wrapElement);
                        }
                    }