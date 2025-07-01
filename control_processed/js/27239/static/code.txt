function(str, polyphone)
        {
            polyphone = polyphone == undefined ? false : polyphone;
            if(!str || /^ +$/g.test(str)) return '';
            if(dict.firstletter) // 使用首字母字典文件
            {
                var result = [];
                for(var i=0; i<str.length; i++)
                {
                    var unicode = str.charCodeAt(i);
                    var ch = str.charAt(i);
                    if(unicode >= 19968 && unicode <= 40869)
                    {
                        ch = dict.firstletter.all.charAt(unicode-19968);
                        if(polyphone) ch = dict.firstletter.polyphone[unicode] || ch;
                    }
                    result.push(ch);
                }
                if(!polyphone) return result.join(''); // 如果不用管多音字，直接将数组拼接成字符串
                else return handlePolyphone(result, '', ''); // 处理多音字，此时的result类似于：['D', 'ZC', 'F']
            }
            else
            {
                var py = this.getPinyin(str, ' ', false, polyphone);
                py = py instanceof Array ? py : [py];
                var result = [];
                for(var i=0; i<py.length; i++)
                {
                    result.push(py[i].replace(/(^| )(\w)\w*/g, function(m,$1,$2){return $2.toUpperCase();}));
                }
                if(!polyphone) return result[0];
                else return simpleUnique(result);
            }
        }