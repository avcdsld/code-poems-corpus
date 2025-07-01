function(time) {

    // Only proceed for agendaWeek view
    if (calendarTarget.fullCalendar('getView').name !== 'agendaWeek'){
      return;
    }

    // Get height of each hour row
    var slotDuration = calendarTarget.fullCalendar('option', 'slotDuration');
    var slotDurationMinutes = 30;
    if (slotDuration) slotDurationMinutes = slotDuration.slice(3, 5);
    var hours = calendarTarget.find('.fc-slats .fc-minor');
    var hourHeight = $(hours[0]).height() * (60 / slotDurationMinutes);

    // If minTime is set in fullCalendar config, subtract that from the scollTo calculationn
    var minTimeHeight = 0;
    if (getConfig().fullcalendar.minTime) {
      var minTime = moment(getConfig().fullcalendar.minTime, 'HH:mm:ss').format('H');
      minTimeHeight = hourHeight * minTime;
    }

    // Calculate scrolling location and container sizes
    var scrollTo = (hourHeight * time) - minTimeHeight;
    var scrollable = calendarTarget.find('.fc-scroller');
    var scrollableHeight = scrollable.height();
    var scrollableScrollTop = scrollable.scrollTop();
    var maximumHeight = scrollable.find('.fc-time-grid').height();

    // Only perform the scroll if the scrollTo is outside the current visible boundary
    if (scrollTo > scrollableScrollTop && scrollTo < scrollableScrollTop + scrollableHeight) {
      return;
    }

    // If scrollTo point is past the maximum height, then scroll to maximum possible while still animating
    if (scrollTo > maximumHeight - scrollableHeight) {
      scrollTo = maximumHeight - scrollableHeight;
    }

    // Perform the scrollTo animation
    scrollable.animate({scrollTop: scrollTo});

  }