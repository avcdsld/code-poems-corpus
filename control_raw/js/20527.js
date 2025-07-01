function meaningfulAttrsChanged() {
                    if (_isSleeping || _mutationObserversConnected)
                        return false;

                    var hostElementId = _hostElement.attr(LEXICON.i) || _strEmpty;
                    var hostElementIdChanged = checkCacheSingle(hostElementId, _updateAutoHostElementIdCache);
                    var hostElementClass = _hostElement.attr(LEXICON.c) || _strEmpty;
                    var hostElementClassChanged = checkCacheSingle(hostElementClass, _updateAutoHostElementClassCache);
                    var hostElementStyle = _hostElement.attr(LEXICON.s) || _strEmpty;
                    var hostElementStyleChanged = checkCacheSingle(hostElementStyle, _updateAutoHostElementStyleCache);
                    var hostElementVisible = _hostElement.is(':visible') || _strEmpty;
                    var hostElementVisibleChanged = checkCacheSingle(hostElementVisible, _updateAutoHostElementVisibleCache);
                    var targetElementRows = _isTextarea ? (_targetElement.attr('rows') || _strEmpty) : _strEmpty;
                    var targetElementRowsChanged = checkCacheSingle(targetElementRows, _updateAutoTargetElementRowsCache);
                    var targetElementCols = _isTextarea ? (_targetElement.attr('cols') || _strEmpty) : _strEmpty;
                    var targetElementColsChanged = checkCacheSingle(targetElementCols, _updateAutoTargetElementColsCache);
                    var targetElementWrap = _isTextarea ? (_targetElement.attr('wrap') || _strEmpty) : _strEmpty;
                    var targetElementWrapChanged = checkCacheSingle(targetElementWrap, _updateAutoTargetElementWrapCache);

                    _updateAutoHostElementIdCache = hostElementId;
                    if (hostElementClassChanged)
                        hostElementClassChanged = hostClassNamesChanged(_updateAutoHostElementClassCache, hostElementClass);
                    _updateAutoHostElementClassCache = hostElementClass;
                    _updateAutoHostElementStyleCache = hostElementStyle;
                    _updateAutoHostElementVisibleCache = hostElementVisible;
                    _updateAutoTargetElementRowsCache = targetElementRows;
                    _updateAutoTargetElementColsCache = targetElementCols;
                    _updateAutoTargetElementWrapCache = targetElementWrap;

                    return hostElementIdChanged || hostElementClassChanged || hostElementStyleChanged || hostElementVisibleChanged || targetElementRowsChanged || targetElementColsChanged || targetElementWrapChanged;
                }