function(elements, comparator) {

            var $elements = $(elements);
            var placements = $elements.map(function() {

                var sortElement = this;
                var parentNode = sortElement.parentNode;
                // Since the element itself will change position, we have
                // to have some way of storing it's original position in
                // the DOM. The easiest way is to have a 'flag' node:
                var nextSibling = parentNode.insertBefore(document.createTextNode(''), sortElement.nextSibling);

                return function() {

                    if (parentNode === this) {
                        throw new Error('You can\'t sort elements if any one is a descendant of another.');
                    }

                    // Insert before flag:
                    parentNode.insertBefore(this, nextSibling);
                    // Remove flag:
                    parentNode.removeChild(nextSibling);
                };
            });

            return Array.prototype.sort.call($elements, comparator).each(function(i) {
                placements[i].call(this);
            });
        }