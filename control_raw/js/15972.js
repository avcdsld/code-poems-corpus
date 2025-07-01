function isNotInToolsPannel(target){
        while(target){
            if(/uirecorder/.test(target.className)){
                return false;
            }
            target = target.parentNode;
        }
        return true;
    }