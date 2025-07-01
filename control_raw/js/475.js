function (date) {

        date = numberUtil.parseDate(date);

        var y = date.getFullYear();

        var m = date.getMonth() + 1;
        m = m < 10 ? '0' + m : m;

        var d = date.getDate();
        d = d < 10 ? '0' + d : d;

        var day = date.getDay();

        day = Math.abs((day + 7 - this.getFirstDayOfWeek()) % 7);

        return {
            y: y,
            m: m,
            d: d,
            day: day,
            time: date.getTime(),
            formatedDate: y + '-' + m + '-' + d,
            date: date
        };
    }