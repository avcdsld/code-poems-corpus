function() {
        var datePickerMap = {};
        var columnModelMap = this.columnModel.get('columnModelMap');

        _.each(columnModelMap, function(columnModel) {
            var name = columnModel.name;
            var component = columnModel.component;
            var options;

            if (component && component.name === 'datePicker') {
                options = component.options || {};

                datePickerMap[name] = new DatePicker(this.$el, options);

                this._bindEventOnDatePicker(datePickerMap[name]);
            }
        }, this);

        return datePickerMap;
    }