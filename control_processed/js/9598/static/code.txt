function calendarDirective() {
    return {
      template:
        '<table aria-hidden="true" class="md-calendar-day-header"><thead></thead></table>' +
        '<div class="md-calendar-scroll-mask">' +
        '<md-virtual-repeat-container class="md-calendar-scroll-container" ' +
              'md-offset-size="' + (TBODY_SINGLE_ROW_HEIGHT - TBODY_HEIGHT) + '">' +
            '<table role="grid" tabindex="0" class="md-calendar" aria-readonly="true">' +
              '<tbody ' +
                  'md-calendar-month-body ' +
                  'role="rowgroup" ' +
                  'md-virtual-repeat="i in monthCtrl.items" ' +
                  'md-month-offset="$index" ' +
                  'class="md-calendar-month" ' +
                  'md-start-index="monthCtrl.getSelectedMonthIndex()" ' +
                  'md-item-size="' + TBODY_HEIGHT + '">' +

                // The <tr> ensures that the <tbody> will always have the
                // proper height, even if it's empty. If it's content is
                // compiled, the <tr> will be overwritten.
                '<tr aria-hidden="true" md-force-height="\'' + TBODY_HEIGHT + 'px\'"></tr>' +
              '</tbody>' +
            '</table>' +
          '</md-virtual-repeat-container>' +
        '</div>',
      require: ['^^mdCalendar', 'mdCalendarMonth'],
      controller: CalendarMonthCtrl,
      controllerAs: 'monthCtrl',
      bindToController: true,
      link: function(scope, element, attrs, controllers) {
        var calendarCtrl = controllers[0];
        var monthCtrl = controllers[1];
        monthCtrl.initialize(calendarCtrl);
      }
    };
  }