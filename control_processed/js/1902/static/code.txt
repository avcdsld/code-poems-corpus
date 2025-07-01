function handleEntryPoint ( index, value, that ) {

        var percentage;

        // Wrap numerical input in an array.
        if ( typeof value === "number" ) {
            value = [value];
        }

        // Reject any invalid input, by testing whether value is an array.
        if ( Object.prototype.toString.call( value ) !== '[object Array]' ){
            throw new Error("noUiSlider: 'range' contains invalid value.");
        }

        // Covert min/max syntax to 0 and 100.
        if ( index === 'min' ) {
            percentage = 0;
        } else if ( index === 'max' ) {
            percentage = 100;
        } else {
            percentage = parseFloat( index );
        }

        // Check for correct input.
        if ( !isNumeric( percentage ) || !isNumeric( value[0] ) ) {
            throw new Error("noUiSlider: 'range' value isn't numeric.");
        }

        // Store values.
        that.xPct.push( percentage );
        that.xVal.push( value[0] );

        // NaN will evaluate to false too, but to keep
        // logging clear, set step explicitly. Make sure
        // not to override the 'step' setting with false.
        if ( !percentage ) {
            if ( !isNaN( value[1] ) ) {
                that.xSteps[0] = value[1];
            }
        } else {
            that.xSteps.push( isNaN(value[1]) ? false : value[1] );
        }

        that.xHighestCompleteStep.push(0);
    }