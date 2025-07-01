function checkAppear() {
        if(scroll.delta < opts.delta.speed) {
          if(!deltaSet) {
            deltaSet = true;
            doCheckAppear();
            setTimeout(function(){
              deltaSet = false;
            }, opts.delta.timeout);
          }
        }
        (debounce(function() {
          doCheckAppear();
        }, opts.debounce)());
      }