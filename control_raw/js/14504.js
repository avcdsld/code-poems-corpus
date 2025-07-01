function onDeactivateEvent() {
         // release pointer events
         me.input.releasePointerEvent("pointerdown", this);
         me.input.releasePointerEvent("pointerup", this);
         me.input.releasePointerEvent("pointercancel", this);
         me.input.releasePointerEvent("pointerenter", this);
         me.input.releasePointerEvent("pointerleave", this);
         me.timer.clearTimeout(this.holdTimeout);
       }