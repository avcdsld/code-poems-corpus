function updateDropdownMenuHeight() {
            if (positionTarget) {
                registerDropdownToggle(angular.element(positionTarget));
            }

            if (!angular.element(dropdownToggle).is(':visible')) {
                return;
            }

            var availableHeight = getAvailableHeight();
            var scrollPosition = dropdownMenu.scrollTop();

            dropdownMenu.css({
                height: 'auto',
            });
            dropdownMenu.css(availableHeight.direction, 'auto');

            var dropdownMenuHeight = dropdownMenu.find('.dropdown-menu__content').outerHeight();

            if ((availableHeight[availableHeight.direction] - ~~lxDropdown.offset) <= dropdownMenuHeight) {
                if (availableHeight.direction === 'top') {
                    dropdownMenu.css({
                        top: 0,
                    });
                } else if (availableHeight.direction === 'bottom') {
                    dropdownMenu.css({
                        bottom: 0,
                    });
                }
            } else {
                if (availableHeight.direction === 'top') {
                    dropdownMenu.css({
                        top: 'auto',
                    });
                } else if (availableHeight.direction === 'bottom') {
                    dropdownMenu.css({
                        bottom: 'auto',
                    });
                }
            }

            dropdownMenu.scrollTop(scrollPosition);
        }