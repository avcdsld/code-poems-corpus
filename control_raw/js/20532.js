function setupStructureDOM(destroy) {
                    var adoptAttrs = _currentPreparedOptions.textarea.inheritedAttrs;
                    var adoptAttrsMap = { };
                    var applyAdoptedAttrs = function() {
                        var applyAdoptedAttrsElm = destroy ? _targetElement : _hostElement;
                        FRAMEWORK.each(adoptAttrsMap, function(k, v) {
                            if(type(v) == TYPES.s) {
                                if(k == LEXICON.c)
                                    applyAdoptedAttrsElm.addClass(v);
                                else
                                    applyAdoptedAttrsElm.attr(k, v);
                            }
                        });
                    };
                    var hostElementClassNames = [
                        _classNameHostElement,
                        _classNameHostTextareaElement,
                        _classNameHostResizeDisabled,
                        _classNameHostRTL,
                        _classNameHostScrollbarHorizontalHidden,
                        _classNameHostScrollbarVerticalHidden,
                        _classNameHostTransition,
                        _classNameHostScrolling,
                        _classNameHostOverflow,
                        _classNameHostOverflowX,
                        _classNameHostOverflowY,
                        _classNameThemeNone,
                        _classNameTextareaElement,
                        _classNameTextInherit,
                        _classNameCache].join(_strSpace);
                    adoptAttrs = type(adoptAttrs) == TYPES.s ? adoptAttrs.split(' ') : adoptAttrs;
                    if(type(adoptAttrs) == TYPES.a) {
                        FRAMEWORK.each(adoptAttrs, function(i, v) {
                            if(type(v) == TYPES.s)
                                adoptAttrsMap[v] = destroy ? _hostElement.attr(v) : _targetElement.attr(v);
                        });
                    }

                    if(!destroy) {
                        if (_isTextarea) {
                            var hostElementCSS = {};
                            var parent = _targetElement.parent();
                            _isTextareaHostGenerated = !(parent.hasClass(_classNameHostTextareaElement) && parent.children()[LEXICON.l] === 1);

                            if (!_currentPreparedOptions.sizeAutoCapable) {
                                hostElementCSS[_strWidth] = _targetElement.css(_strWidth);
                                hostElementCSS[_strHeight] = _targetElement.css(_strHeight);
                            }
                            if(_isTextareaHostGenerated)
                                _targetElement.wrap(generateDiv(_classNameHostTextareaElement));

                            _hostElement = _targetElement.parent();
                            _hostElement.css(hostElementCSS)
                                .wrapInner(generateDiv(_classNameContentElement + _strSpace + _classNameTextInherit))
                                .wrapInner(generateDiv(_classNameViewportElement + _strSpace + _classNameTextInherit))
                                .wrapInner(generateDiv(_classNamePaddingElement + _strSpace + _classNameTextInherit));
                            _contentElement = findFirst(_hostElement, _strDot + _classNameContentElement);
                            _viewportElement = findFirst(_hostElement, _strDot + _classNameViewportElement);
                            _paddingElement = findFirst(_hostElement, _strDot + _classNamePaddingElement);
                            _textareaCoverElement = FRAMEWORK(generateDiv(_classNameTextareaCoverElement));
                            _contentElement.prepend(_textareaCoverElement);

                            addClass(_targetElement, _classNameTextareaElement + _strSpace + _classNameTextInherit);

                            if(_isTextareaHostGenerated)
                                applyAdoptedAttrs();
                        }
                        else {
                            _hostElement = _targetElement;
                            _hostElement.wrapInner(generateDiv(_classNameContentElement))
                                .wrapInner(generateDiv(_classNameViewportElement))
                                .wrapInner(generateDiv(_classNamePaddingElement));
                            _contentElement = findFirst(_hostElement, _strDot + _classNameContentElement);
                            _viewportElement = findFirst(_hostElement, _strDot + _classNameViewportElement);
                            _paddingElement = findFirst(_hostElement, _strDot + _classNamePaddingElement);

                            addClass(_targetElement, _classNameHostElement);
                        }

                        if (_nativeScrollbarStyling)
                            addClass(_viewportElement, _nativeScrollbarIsOverlaid.x && _nativeScrollbarIsOverlaid.y ? _classNameViewportNativeScrollbarsOverlaid : _classNameViewportNativeScrollbarsInvisible);
                        if (_isBody)
                            addClass(_htmlElement, _classNameHTMLElement);

                        _sizeObserverElement = FRAMEWORK(generateDiv('os-resize-observer-host'));
                        _hostElement.prepend(_sizeObserverElement);

                        _sizeObserverElementNative = _sizeObserverElement[0];
                        _hostElementNative = _hostElement[0];
                        _paddingElementNative = _paddingElement[0];
                        _viewportElementNative = _viewportElement[0];
                        _contentElementNative = _contentElement[0];
                    }
                    else {
                        _contentElement.contents()
                            .unwrap()
                            .unwrap()
                            .unwrap();

                        removeClass(_hostElement, hostElementClassNames);
                        if (_isTextarea) {
                            _targetElement.removeAttr(LEXICON.s);

                            if(_isTextareaHostGenerated)
                                applyAdoptedAttrs();

                            removeClass(_targetElement, hostElementClassNames);
                            remove(_textareaCoverElement);

                            if(_isTextareaHostGenerated) {
                                _targetElement.unwrap();
                                remove(_hostElement);
                            }
                            else {
                                addClass(_hostElement, _classNameHostTextareaElement);
                            }
                        }
                        else {
                            removeClass(_targetElement, _classNameHostElement);
                        }

                        if (_isBody)
                            removeClass(_htmlElement, _classNameHTMLElement);

                        remove(_sizeObserverElement);
                    }
                }