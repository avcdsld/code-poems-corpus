public static void compileWithoutNS(List<IWord> wordList)
    {
        for (IWord word : wordList)
        {
            if (word.getLabel().startsWith("ns")) continue;
            word.setValue(PosTagCompiler.compile(word.getLabel(), word.getValue()));
//            switch (word.getLabel())
//            {
//                case "nx":
//                {
//                    word.setValue(Predefine.TAG_PROPER);
//                }
//                break;
//                case "nt":
//                case "ntc":
//                case "ntcf":
//                case "ntcb":
//                case "ntch":
//                case "nto":
//                case "ntu":
//                case "nts":
//                case "nth":
//                {
//                    word.setValue(Predefine.TAG_GROUP);
//                }
//                break;
//                case "m":
//                case "mq":
//                {
//                    word.setValue(Predefine.TAG_NUMBER);
//                }
//                break;
//                case "x":
//                {
//                    word.setValue(Predefine.TAG_CLUSTER);
//                }
//                break;
//                case "xx":
//                {
//                    word.setValue(Predefine.TAG_OTHER);
//                }
//                break;
//                case "t":
//                {
//                    word.setValue(Predefine.TAG_TIME);
//                }
//                break;
//                case "nr":
//                {
//                    word.setValue(Predefine.TAG_PEOPLE);
//                }
//                break;
//            }
        }
    }