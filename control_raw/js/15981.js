function checkLostKey(windowId){
    if(windowId !== lastWindow){
        if(lastWindow !== -1){
            var cmdInfo;
            for(var key in allKeyMap){
                cmdInfo = allKeyMap[key];
                execNextCommand({
                    window: cmdInfo.window,
                    frame: cmdInfo.frame,
                    cmd: 'keyUp',
                    data: cmdInfo.data,
                    fix: true
                });
            }
            allKeyMap = {};
            for(var button in allMouseMap){
                cmdInfo = allMouseMap[button];
                execNextCommand({
                    window: cmdInfo.window,
                    frame: cmdInfo.frame,
                    cmd: 'mouseUp',
                    data: cmdInfo.data,
                    fix: true
                });
            }
            allMouseMap = {};
        }
        lastWindow = windowId;
    }
}