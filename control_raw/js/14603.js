function onPointerEvent(e) {
       var ret = true; // normalize eventTypes

       normalizeEvent(e); // remember/use the first "primary" normalized event for pointer.bind

       var button = normalizedEvents[0].button; // dispatch event to registered objects

       if (dispatchEvent(normalizedEvents) || api.preventDefault) {
         // prevent default action
         ret = api._preventDefaultFn(e);
       }

       var keycode = api.pointer.bind[button]; // check if mapped to a key

       if (keycode) {
         if (POINTER_DOWN.includes(e.type)) {
           return api._keydown(e, keycode, button + 1);
         } else {
           // 'mouseup' or 'touchend'
           return api._keyup(e, keycode, button + 1);
         }
       }

       return ret;
     }