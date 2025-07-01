function() {
            var $this = $(this);
            $this.find('.treegrid-indent').remove();
            var tpl = $this.treegrid('getSetting', 'indentTemplate');
            var expander = $this.find('.treegrid-expander');
            var depth = $this.treegrid('getDepth');
            for (var i = 0; i < depth; i++) {
                $(tpl).insertBefore(expander);
            }
            return $this;
        }