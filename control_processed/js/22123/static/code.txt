function(target) {
            if (typeof target == 'string') {
                target = document.querySelector(target);
            }
            if (!target) return;
            var protocol = target.getAttribute('minder-data-type');
            if (protocol in protocols) {
                var data = target.textContent;
                target.textContent = null;
                this.renderTo(target);
                this.importData(protocol, data);
            }
            return this;
        }