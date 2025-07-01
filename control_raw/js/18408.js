function getNativeScrollbarWidth(container) {
            var container = container ? container : document.body;

            var fullWidth = 0;
            var barWidth = 0;

            var wrapper = document.createElement('div');
            var child = document.createElement('div');

            wrapper.style.position = 'absolute';
            wrapper.style.pointerEvents = 'none';
            wrapper.style.bottom = '0';
            wrapper.style.right = '0';
            wrapper.style.width = '100px';
            wrapper.style.overflow = 'hidden';

            wrapper.appendChild(child);
            container.appendChild(wrapper);

            fullWidth = child.offsetWidth;
            child.style.width = '100%';
            wrapper.style.overflowY = 'scroll';
            barWidth = fullWidth - child.offsetWidth;

            container.removeChild(wrapper);

            return barWidth;
        }