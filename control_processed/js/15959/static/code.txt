function getDomPath(target, isAllDom){
        var arrAllPaths = [];
        var node = target, path;
        while(node){
            var nodeName = node.nodeName.toLowerCase();
            if(/^#document/.test(nodeName)){
                path = getRelativeDomPath(node, target, isAllDom);
                if(path){
                    arrAllPaths.push(path);
                }
                node = node.parentNode || node.host;
                target = node;
            }
            else{
                node = node.parentNode || node.host;
            }
        }
        return arrAllPaths.length > 0 ? arrAllPaths.reverse().join(' /deep/ ') : null;
    }