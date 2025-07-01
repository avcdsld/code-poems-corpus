function byteLen(text){
        var count = 0;
        for(var i=0,len=text.length;i<len;i++){
            char = text.charCodeAt(i);
            count += char > 255 ? 2 : 1;
        }
        return count;
    }