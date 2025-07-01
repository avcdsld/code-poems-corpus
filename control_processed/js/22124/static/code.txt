function(json) {
            if (!json) return;

            /**
             * @event preimport
             * @for Minder
             * @when 导入数据之前
             */
            this._fire(new MinderEvent('preimport', null, false));

            // 删除当前所有节点
            while (this._root.getChildren().length) {
                this.removeNode(this._root.getChildren()[0]);
            }

            json = compatibility(json);

            this.importNode(this._root, json.root);

            this.setTemplate(json.template || 'default');
            this.setTheme(json.theme || null);
            this.refresh();

            /**
             * @event import,contentchange,interactchange
             * @for Minder
             * @when 导入数据之后
             */
            this.fire('import');

            this._firePharse({
                type: 'contentchange'
            });

            this._interactChange();

            return this;
        }