function hookAlertFunction(){
            var rawAlert = window.alert;
            function sendAlertCmd(cmd, data){
                var cmdInfo = {
                    cmd: cmd,
                    data: data || {}
                };
                window.postMessage({
                    'type': 'uiRecorderAlertCommand',
                    'cmdInfo': cmdInfo
                }, '*');
            }
            window.alert = function(str){
                var ret = rawAlert.call(this, str);
                sendAlertCmd('acceptAlert');
                return ret;
            }
            var rawConfirm = window.confirm;
            window.confirm = function(str){
                var ret = rawConfirm.call(this, str);
                sendAlertCmd(ret?'acceptAlert':'dismissAlert');
                return ret;
            }
            var rawPrompt = window.prompt;
            window.prompt = function(str){
                var ret = rawPrompt.call(this, str);
                if(ret === null){
                    sendAlertCmd('dismissAlert');
                }
                else{
                    sendAlertCmd('setAlert', {
                        text: ret
                    });
                    sendAlertCmd('acceptAlert');
                }
                return ret;
            }
            function wrapBeforeUnloadListener(oldListener){
                var newListener = function(e){
                    var returnValue = oldListener(e);
                    if(returnValue){
                        sendAlertCmd('acceptAlert');
                    }
                    return returnValue;
                }
                return newListener;
            }
            var rawAddEventListener = window.addEventListener;
            window.addEventListener = function(type, listener, useCapture){
                if(type === 'beforeunload'){
                    listener = wrapBeforeUnloadListener(listener);
                }
                return rawAddEventListener.call(window, type, listener, useCapture);
            };
            setTimeout(function(){
                var oldBeforeunload = window.onbeforeunload;
                if(oldBeforeunload){
                    window.onbeforeunload = wrapBeforeUnloadListener(oldBeforeunload)
                }
            }, 1000);
        }