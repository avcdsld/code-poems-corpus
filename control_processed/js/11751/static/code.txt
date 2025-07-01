function () {
            var t = this,
                documentSelection = t.doc.getSelection(),
                node = documentSelection.focusNode,
                text = new XMLSerializer().serializeToString(documentSelection.getRangeAt(0).cloneContents()),
                url,
                title,
                target;

            while (['A', 'DIV'].indexOf(node.nodeName) < 0) {
                node = node.parentNode;
            }

            if (node && node.nodeName === 'A') {
                var $a = $(node);
                text = $a.text();
                url = $a.attr('href');
                if (!t.o.minimalLinks) {
                    title = $a.attr('title');
                    target = $a.attr('target');
                }
                var range = t.doc.createRange();
                range.selectNode(node);
                documentSelection.removeAllRanges();
                documentSelection.addRange(range);
            }

            t.saveRange();

            var options = {
                url: {
                    label: 'URL',
                    required: true,
                    value: url
                },
                text: {
                    label: t.lang.text,
                    value: text
                }
            };
            if (!t.o.minimalLinks) {
                Object.assign(options, {
                    title: {
                        label: t.lang.title,
                        value: title
                    },
                    target: {
                        label: t.lang.target,
                        value: target
                    }
                });
            }

            t.openModalInsert(t.lang.createLink, options, function (v) { // v is value
                var url = t.prependUrlPrefix(v.url);
                if (!url.length) {
                    return false;
                }

                var link = $(['<a href="', url, '">', v.text || v.url, '</a>'].join(''));

                if (!t.o.minimalLinks) {
                    if (v.title.length > 0) {
                        link.attr('title', v.title);
                    }
                    if (v.target.length > 0) {
                        link.attr('target', v.target);
                    }
                }
                t.range.deleteContents();
                t.range.insertNode(link[0]);
                t.syncCode();
                t.$c.trigger('tbwchange');
                return true;
            });
        }