import flash.utils.Timer;

var steveTimer = new Timer( 1000 );
steveTimer.addEventListener(TimerEvent.TIMER, stillAlive);
steveTimer.start();

function stillAlive(e)
    {
    trace ("Steve tried to killed me, but I've 
    lived " + ( Math.round(new Date().getTime() / 
    1000) - 1317772800 ) + " seconds longer.");
    }
