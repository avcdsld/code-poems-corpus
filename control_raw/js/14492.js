function onDeactivateEvent() {
         // cancel all event subscriptions
         me.event.unsubscribe(this.vpChangeHdlr);
         me.event.unsubscribe(this.vpResizeHdlr);
         me.event.unsubscribe(this.vpLoadedHdlr);
       }