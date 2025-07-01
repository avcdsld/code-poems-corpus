function( options ){

            // call parent init method
            parent.init.call(this, options);

            options = Physics.util.extend({}, defaults, options);

            this.geometry = Physics.geometry('rectangle', {
                width: options.width,
                height: options.height
            });

            this.recalc();
        }