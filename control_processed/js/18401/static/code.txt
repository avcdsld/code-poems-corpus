function hideScrollbarUsingPseudoElement(el){
            var state = getState(el);
            var idName = 'vuebar-pseudo-element-styles';
            var selector = '.' + state.config.el2Class + '::-webkit-scrollbar';
            var styleElm = document.getElementById(idName);
            var sheet = null;

            if (styleElm) {
                sheet = styleElm.sheet;
            } else {
                styleElm = document.createElement('style');
                styleElm.id = idName;
                document.head.appendChild(styleElm);
                sheet = styleElm.sheet;
            }

            // detect if there is a rule already added to the selector
            var ruleExists = false;
            for(var i=0, l=sheet.rules.length; i<l; i++){
                var rule = sheet.rules[i];
                if (rule.selectorText == selector) {
                    ruleExists = true;
                }
            }

            // if there is rule added already then don't continue
            if ( ruleExists ) { return false }

            // insert rule
            // - we only need to use insertRule and don't need to use addRule at all
            //   because we're only targeting chrome & safari browsers
            if (sheet.insertRule) {
                sheet.insertRule(selector + '{display:none}', 0);
            }

        }