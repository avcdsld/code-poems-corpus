function step(){

        var time;

        window.requestAnimationFrame( step );

        if (!active){
            return;
        }

        time = now();

        if (!time){
            return;
        }

        ps.emit( 'tick', time );
    }