private static List<AtomNode> atomSegment(String sSentence, int start, int end)
    {
        if (end < start)
        {
            throw new RuntimeException("start=" + start + " < end=" + end);
        }
        List<AtomNode> atomSegment = new ArrayList<AtomNode>();
        int pCur = 0, nCurType, nNextType;
        StringBuilder sb = new StringBuilder();
        char c;


        //==============================================================================================
        // by zhenyulu:
        //
        // TODO: 使用一系列正则表达式将句子中的完整成分（百分比、日期、电子邮件、URL等）预先提取出来
        //==============================================================================================

        char[] charArray = sSentence.substring(start, end).toCharArray();
        int[] charTypeArray = new int[charArray.length];

        // 生成对应单个汉字的字符类型数组
        for (int i = 0; i < charArray.length; ++i)
        {
            c = charArray[i];
            charTypeArray[i] = CharType.get(c);

            if (c == '.' && i < (charArray.length - 1) && CharType.get(charArray[i + 1]) == CharType.CT_NUM)
                charTypeArray[i] = CharType.CT_NUM;
            else if (c == '.' && i < (charArray.length - 1) && charArray[i + 1] >= '0' && charArray[i + 1] <= '9')
                charTypeArray[i] = CharType.CT_SINGLE;
            else if (charTypeArray[i] == CharType.CT_LETTER)
                charTypeArray[i] = CharType.CT_SINGLE;
        }

        // 根据字符类型数组中的内容完成原子切割
        while (pCur < charArray.length)
        {
            nCurType = charTypeArray[pCur];

            if (nCurType == CharType.CT_CHINESE || nCurType == CharType.CT_INDEX ||
                nCurType == CharType.CT_DELIMITER || nCurType == CharType.CT_OTHER)
            {
                String single = String.valueOf(charArray[pCur]);
                if (single.length() != 0)
                    atomSegment.add(new AtomNode(single, nCurType));
                pCur++;
            }
            //如果是字符、数字或者后面跟随了数字的小数点“.”则一直取下去。
            else if (pCur < charArray.length - 1 && ((nCurType == CharType.CT_SINGLE) || nCurType == CharType.CT_NUM))
            {
                sb.delete(0, sb.length());
                sb.append(charArray[pCur]);

                boolean reachEnd = true;
                while (pCur < charArray.length - 1)
                {
                    nNextType = charTypeArray[++pCur];

                    if (nNextType == nCurType)
                        sb.append(charArray[pCur]);
                    else
                    {
                        reachEnd = false;
                        break;
                    }
                }
                atomSegment.add(new AtomNode(sb.toString(), nCurType));
                if (reachEnd)
                    pCur++;
            }
            // 对于所有其它情况
            else
            {
                atomSegment.add(new AtomNode(charArray[pCur], nCurType));
                pCur++;
            }
        }

//        logger.trace("原子分词:" + atomSegment);
        return atomSegment;
    }