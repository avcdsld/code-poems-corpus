function mdCalendarYearDirective() {
    return {
      require: ['^^mdCalendar', '^^mdCalendarYear', 'mdCalendarYearBody'],
      scope: { offset: '=mdYearOffset' },
      controller: CalendarYearBodyCtrl,
      controllerAs: 'mdYearBodyCtrl',
      bindToController: true,
      link: function(scope, element, attrs, controllers) {
        var calendarCtrl = controllers[0];
        var yearCtrl = controllers[1];
        var yearBodyCtrl = controllers[2];

        yearBodyCtrl.calendarCtrl = calendarCtrl;
        yearBodyCtrl.yearCtrl = yearCtrl;

        scope.$watch(function() { return yearBodyCtrl.offset; }, function(offset) {
          if (angular.isNumber(offset)) {
            yearBodyCtrl.generateContent();
          }
        });
      }
    };
  }